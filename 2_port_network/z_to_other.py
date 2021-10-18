import cmath
import numpy as np
from color import bcolors


def z_to_other():
    z_11 = complex(input("z_11= "))
    z_12 = complex(input("z_12= "))
    z_21 = complex(input("z_21= "))
    z_22 = complex(input("z_22= "))

    delta_z_ = np.array([z_11])*np.array([z_22])-np.array([z_12])*np.array([z_21])
    delta_z = complex(delta_z_[0])

    z = np.array([[z_11, z_12], [z_21, z_22]])
    y = np.linalg.inv(z)

    h_11 = delta_z / z_22
    h_12 = z_12 / z_22
    h_21 = (-1*z_21) / z_22
    h_22 = 1 / z_22
    h = np.array([[h_11, h_12], [h_21, h_22]])

    t_11 = z_11 / z_21
    t_12 = delta_z / z_21
    t_21 = 1 / z_21
    t_22 = z_22 / z_21
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

    if a == d and (a*d - b*c).real - 1 < 0.01:
        print(f"\n{bcolors.WARNING}System is Reciprocal and Symmetric")
        z_0 = cmath.sqrt(b / c)
        e_gamma = a + cmath.sqrt(b * c)
        print(f"characteristic impedance z_0 = +-{z_0} and transfer constant e^gamma = {e_gamma} ")

    elif (a*d - b*c).real - 1 < 0.01:
        print(f"\n{bcolors.WARNING}System is Reciprocal")
        z_img_1 = cmath.sqrt((a*b)/(c*d))
        z_img_2 = cmath.sqrt((d*b)/(c*a))
        e_gamma = cmath.sqrt(a*d) + cmath.sqrt(b*c)
        print(f"z_img_1 = +- {z_img_1} and z_img_2 = +- {z_img_2} and transfer constant e^gamma = {e_gamma} ")

    elif a == d:
        print(f"{bcolors.WARNING}System is Symmetric")

