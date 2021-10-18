import numpy as np
import cmath
from color import bcolors


def t_to_other():
    a = complex(input("A= "))
    b = complex(input("B= "))
    c = complex(input("C= "))
    d = complex(input("D= "))

    delta_t_ = np.array([a])*np.array([d])-np.array([b])*np.array([c])
    delta_t = complex(delta_t_[0])

    t = np.array([[a, b], [c, d]])

    z_11 = a / c
    z_12 = delta_t / c
    z_21 = 1 / c
    z_22 = d / c
    z = np.array([[z_11, z_12], [z_21, z_22]])
    y = np.linalg.inv(z)

    h_11 = b / d
    h_12 = delta_t / d
    h_21 = -1 / d
    h_22 = c / d
    h = np.array([[h_11, h_12], [h_21, h_22]])

    print("\n Z TRANSFORM ")
    print(z)
    print("\n Y TRANSFORM ")
    print(y)
    print("\n H TRANSFORM ")
    print(h)
    print("\n T TRANSFORM ")
    print(t)

    if a == d and (a*d - b*c).real - 1 < 0.01:
        print(f"\n{bcolors.WARNING}System is Reciprocal and Symmetric")
        z_0 = cmath.sqrt(b / c)
        e_gamma = a + cmath.sqrt(b * c)
        print(
            f"characteristic impedance z_0 = +-{z_0} and transfer constant e^gamma = {e_gamma} ")

    elif (a*d - b*c).real - 1 < 0.01:
        print(f"{bcolors.WARNING}System is Reciprocal")
        z_img_1 = cmath.sqrt((a * b) / (c * d))
        z_img_2 = cmath.sqrt((d * b) / (c * a))
        e_gamma = cmath.sqrt(a * d) + cmath.sqrt(b * c)
        print(
            f"z_img_1 = +- {z_img_1} and z_img_2 = +- {z_img_2} and transfer constant e^gamma = +- {e_gamma.real} ")

    elif a == d:
        print(f"{bcolors.WARNING}System is Symmetric")

