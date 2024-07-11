import numpy as np

if __name__ == "__main__":
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(a + b)
    print(a - b)
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print(A + B)
    print(A - B)
    print(np.dot(a, b))
    C = np.array([[1, 2, 3], [4, 5, 6]])
    D = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])
    print(np.dot(C, D))
    print(np.dot(np.dot(C, C.T), C ^ -1))
    print(A.T)
