import numpy as np
import cmath
from color import bcolors


def y_to_other():
    y_11 = complex(input("y_11= "))
    y_12 = complex(input("y_12= "))
    y_21 = complex(input("y_21= "))
    y_22 = complex(input("y_22= "))

    delta_y_ = np.array([y_11])*np.array([y_22])-np.array([y_12])*np.array([y_21])
    delta_y = complex(delta_y_[0])

    y = np.array([[y_11, y_12], [y_21, y_22]])
    z = np.linalg.inv(y)

    h_11 = 1 / y_11
    h_12 = -y_12 / y_11
    h_21 = y_21 / y_11
    h_22 = delta_y / y_11
    h = np.array([[h_11, h_12], [h_21, h_22]])

    t_11 = -y_22 / y_21
    t_12 = -1 / y_21
    t_21 = -delta_y / y_21
    t_22 = -y_11 / y_21
    t = np.array([[t_11, t_12], [t_21, t_22]])

    print("\n Z TRANSFORM ")
    print(z)
    print("\n Y TRANSFORM ")
    print(y)
    print("\n H TRANSFORM ")
    print(h)
    print("\n T TRANSFORM ")
    print(t)

    a = complex(t_11)
    b = complex(t_12)
    c = complex(t_21)
    d = complex(t_22)

    if a == d and (a * d - b * c).real == 1:
        print(f"\n{bcolors.WARNING}System is Reciprocal and Symmetric")
        z_0 = cmath.sqrt(b / c)
        e_gamma = a + cmath.sqrt(b * c)
        print(
            f"characteristic impedance z_0 = +-{z_0} and transfer constant e^gamma = {e_gamma} ")

    elif (a * d - b * c).real == 1:
        print(f"{bcolors.WARNING}System is Reciprocal")
        z_img_1 = cmath.sqrt((a * b) / (c * d))
        z_img_2 = cmath.sqrt((d * b) / (c * a))
        e_gamma = cmath.sqrt(a * d) + cmath.sqrt(b * c)
        print(
            f"z_img_1 = +- {z_img_1} and z_img_2 = +- {z_img_2} and transfer constant e^gamma = +- {e_gamma.real} ")

    elif a == d:
        print(f"{bcolors.WARNING}System is Symmetric")



