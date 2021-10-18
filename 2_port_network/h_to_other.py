import numpy as np
import cmath
from color import bcolors


def h_to_other():
    h_11 = complex(input("h_11= "))
    h_12 = complex(input("h_12= "))
    h_21 = complex(input("h_21= "))
    h_22 = complex(input("h_22= "))

    delta_h_ = np.array([h_11])*np.array([h_22])-np.array([h_12])*np.array([h_21])
    delta_h = complex(delta_h_[0])

    h = np.array([[h_11, h_12], [h_21, h_22]])

    z_11 = delta_h / h_22
    z_12 = h_12 / h_22
    z_21 = -h_21 / h_22
    z_22 = 1 / h_22
    z = np.array([[z_11, z_12], [z_21, z_22]])
    y = np.linalg.inv(z)

    t_11 = -delta_h / h_21
    t_12 = -h_11 / h_21
    t_21 = -h_22 / h_21
    t_22 = -1 / h_21
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

