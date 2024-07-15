import unittest
import physics
import math
import numpy as np


class testphysics(unittest.TestCase):
    def test_calc_weight(self):
        self.assertAlmostEqual(physics.calc_weight(0), 0)
        self.assertAlmostEqual(physics.calc_weight(1), 9.81)
        self.assertAlmostEqual(physics.calc_weight(-1), -9.81)
        self.assertAlmostEqual(physics.calc_weight(1000), 9810)

    def test_calc_buoyancy(self):
        with self.assertRaises(ValueError):
            physics.calc_buoyancy(0, 1000)
        with self.assertRaises(ValueError):
            physics.calc_buoyancy(1000, 0)
        # self.assertRaises( physics.calc_buoyancy(0, 1000),ValueError)
        # self.assertRaises( physics.calc_buoyancy(1000, 0), ValueError)
        self.assertAlmostEqual(physics.calc_buoyancy(1, 1000), 9810)
        self.assertAlmostEqual(physics.calc_buoyancy(0.5, 500), 2452.5)

    def test_will_float(self):
        with self.assertRaises(ValueError):
            physics.will_float(0, 1)
        self.assertTrue(physics.will_float(1, 1))
        self.assertFalse(physics.will_float(0.1, 1000))
        self.assertTrue(physics.will_float(1000, 1000))

    def test_calc_pressure(self):
        self.assertAlmostEqual(physics.calc_pressure(0), 0)
        self.assertAlmostEqual(physics.calc_pressure(10), 98100)
        self.assertAlmostEqual(physics.calc_pressure(100), 981000)

    def test_calc_accel(self):
        self.assertAlmostEqual(physics.calc_accel(0, 1), 0)
        self.assertAlmostEqual(physics.calc_accel(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            physics.calc_accel(1, 0)

    def test_calc_ang_accel(self):
        self.assertAlmostEqual(physics.calc_ang_accel(0, 1), 0)
        self.assertAlmostEqual(physics.calc_ang_accel(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            physics.calc_ang_accel(10, 0)

    def test_calc_torque(self):
        self.assertAlmostEqual(physics.calc_torque(0, 0, 1), 0)
        self.assertAlmostEqual(physics.calc_torque(10, 0, 1), 0)
        self.assertAlmostEqual(physics.calc_torque(10, math.pi / 2, 1), 10)
        with self.assertRaises(ValueError):
            physics.calc_torque(10, 10, 0)

    def test_calculate_mom_inertia(self):
        self.assertAlmostEqual(physics.calculate_mom_inertia(0, 1), 0)
        self.assertAlmostEqual(physics.calculate_mom_inertia(1, 0), 0)
        self.assertAlmostEqual(physics.calculate_mom_inertia(2, 3), 18)

    def test_calculate_auv_accel(self):
        np.testing.assert_array_almost_equal(
            physics.calculate_auv_accel(0, 0), np.array([0, 0])
        )
        np.testing.assert_array_almost_equal(
            physics.calculate_auv_accel(10, 0), np.array([0.1, 0])
        )
        np.testing.assert_array_almost_equal(
            physics.calculate_auv_accel(10, math.pi / 2), np.array([0, 0.1])
        )

    def test_calculate_auv_ang_accel(self):
        self.assertAlmostEqual(physics.calculate_auv_ang_accel(0, 0), 0)
        self.assertAlmostEqual(physics.calculate_auv_ang_accel(10, 0), 0)
        self.assertAlmostEqual(physics.calculate_auv_ang_accel(10, math.pi / 2), 5)

    def test_calc_auv2_accel(self):
        T = np.array([1, 0, 0, 1])
        alpha = math.pi / 4
        theta = 0
        np.testing.assert_array_equal(
            physics.calc_auv2_accel(T * 0, alpha, theta), np.array([0, 0])
        )
        print(physics.calc_auv2_accel(T, alpha + 100, theta + 123))
        np.testing.assert_equal(
            np.any(
                np.not_equal(
                    physics.calc_auv2_accel(T, alpha + 100, theta + 123),
                    np.array([0, 0]),
                )
            ),
            True,
        )
        np.testing.assert_equal(
            physics.calc_auv2_accel(T * 3, alpha + math.pi / 4, theta),
            np.array([0, 0.06]),
        )
        np.testing.assert_almost_equal(
            physics.calc_auv2_accel(T * 3, alpha + math.pi / 4, theta + math.pi / 2),
            np.array([-0.06, 0]),
        )

    def test_calc_auv2_ang_accel(self):
        T = np.array([1, 1, 1, 1])
        alpha = math.pi / 4
        L = 1
        l = 1
        T1 = np.array([1,0,0,0])
        self.assertAlmostEqual(physics.calc_auv2_ang_accel(T, alpha, L, l), 0)
        self.assertEqual(physics.calc_auv2_ang_accel(T,alpha,L,l), 1)
        self.assertNotEqual(physics.calc_auv2_ang_accel(T, alpha + math.pi/2, 10, 23), 1)


if __name__ == "__main__":
    unittest.main()
