import numpy as np
import math


def calc_weight(mass):
    """utility func that calculates F_g from mass in kg on earth"""
    return 9.81 * mass


def calc_buoyancy(V, density):
    """calculates density when given volume in cubic meters
    and density in kg/m^3, using earths g constant"""
    if V <= 0:
        raise ValueError("can't have no volume")
    if density <= 0:
        raise ValueError("can't have 0 density")
    return V * density * 9.81


def will_float(V, mass):
    """calculates if an object will float given mass in
    kg and volume in m^3"""
    if V == 0:
        raise ValueError("can't have no volume")
    if calc_buoyancy(V, 1000) > calc_weight(mass):
        return True
    return False


def calc_pressure(depth):
    """calculates pressure in water on earth given depth in meters, returning in pascals."""
    if depth > 0:
        return depth * 9.81 * 1000 + 101325
    if depth <= 0:
        return 101325 + 9.81 * depth * 1.325


def calc_accel(force, mass):
    """calculates acceleration in m/s^2 give force in N and mass in kg"""
    if mass <= 0:
        raise ZeroDivisionError("can't divide by 0 or negative mass")
    return force / mass


def calc_ang_accel(tau, I):
    """calculates angular acceleration given torque in Nm and moment of inertia in kg*m^2"""
    if I <= 0:
        raise ZeroDivisionError("can't divide by 0 or negative mass")
    return tau / I


def calc_torque(Fmag, Fdir, r):
    """calculates a torque in Newton meters given its magnitude in Newtons, direction in radains, and distance from axis of rotation in meters."""
    if r <= 0:
        raise ValueError("can't have 0 or negative radius")
    return r * Fmag * math.sin(Fdir)


def calculate_mom_inertia(m, r):
    """calculates moment of inertia given the mass of an object in kgs and the distance from axis of rotation in meters"""
    return m * r * r


def calculate_auv_accel(Fmag, Fdir, mass=100, volume=0.1, thruster_dist=0.5):
    """given a force and its angle in newtons and radians, with option to change mass in kg, volume in m^3, and thruster distance in m, returns the translation acceleration of the vehicle in a 2d vector format in m/s^2."""
    if mass <= 0 or volume <= 0:
        raise ValueError("can't have 0/negative mass/volume")
    # F_vertical = Fmag * math.sin(Fdir)
    # F_horizontal = Fmag * math.cos(Fdir)
    F = Fmag * np.array([np.cos(Fdir), np.sin(Fdir)])
    return F / mass


def calculate_auv_ang_accel(Fmag, Fdir, interia=1, thruster_dist=0.5):
    """given a force and its angle, with option to change inertia and thruster distance, returns the rotational acceleration of the vehicle with a thruster in the center axis."""
    if interia <= 0:
        raise ZeroDivisionError("can't divide by 0/ negative interia")
    return Fmag * math.sin(Fdir) * thruster_dist / interia


def calc_auv2_accel(T, alpha, theta, mass=100):
    """given a np array of forces in newtons, an alpha offset of the motor in radians, and a theta offset of the vehicle in radians, and the mass of the vehicle  in kgs, reutrns the a 2d array of the vehicle's accleration in m/s^2"""
    if mass <= 0:
        raise ZeroDivisionError("can't divide by 0/negative mass")
    Thorz = T * math.cos(alpha)
    Tvert = T * math.sin(alpha)
    tothorizontal = Thorz[0] + Thorz[1] - Thorz[2] - Thorz[3]
    totvertical = Tvert[0] - Tvert[1] - Tvert[2] + Tvert[3]
    accel = np.array([tothorizontal, totvertical])
    rotate = np.array(
        [[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]]
    )
    return np.dot(rotate, accel) / mass


def calc_auv2_ang_accel(T, alpha, L, l, interia=100):
    Thorz = T * np.sin(alpha)
    Tvert = T * np.cos(alpha)
    torques = l * Thorz + L * Tvert
    return torques[0] - torques[1] + torques[2] - torques[3]


def sim_auv_motion(
    T, alpha, L, l, lmass, inertia, dt=0.1, t_final=10, x0=0, y0=0, theta=0
):
    count = 0
    curang = theta
    timestamps = np.array([0])
    x = np.array([x0])
    y = np.array([y0])
    theta = np.array([theta])
    v = np.array([0, 0])
    omega = np.array([0])
    a = np.array([0, 0])
    while count <= t_final:
        count += dt
        timestamps = np.append(timestamps, count)
        accel = calc_auv2_accel(T, alpha, curang)
        a = np.append(a, accel)
        angaccel = calc_auv2_ang_accel(T, alpha, L, l, inertia)
        newv = v[-1] + accel * dt
        newomega = omega[-1] + angaccel * dt
        v = np.append(v, newv)
        omega = np.append(omega, newomega)
        newtheta = theta[-1] * dt + 0.5 * angaccel * dt * dt
        theta = np.append(theta, newtheta)
        curang = theta
        newcoords = np.array([x[-1], y[-1]]) * dt + 0.5 * accel * dt * dt
        x = np.append(x, newcoords[0])
        y = np.append(y, newcoords[1])
    return timestamps, x, y, theta, v, omega, a


if __name__ == "__main__":
    T = np.array([1, 0, 1, 0])
    alpha = 0
    L = 4
    l = 3
    print(calc_auv2_ang_accel(T, alpha, L, l))
