import numpy as np
from image_parameter import *


def z_to_other():
    z_11 = complex(input("z_11= "))
    z_12 = complex(input("z_12= "))
    z_21 = complex(input("z_21= "))
    z_22 = complex(input("z_22= "))

    delta_z_ = np.array([z_11]) * np.array([z_22]) - np.array([z_12]) * np.array([z_21])
    delta_z = complex(delta_z_[0])

    z = np.array([[z_11, z_12], [z_21, z_22]])

    try:
        y = np.linalg.inv(z)
    except:
        y = "Cannot find as delta_z = 0"

    try:
        h_11 = delta_z / z_22
        h_12 = z_12 / z_22
        h_21 = (-1 * z_21) / z_22
        h_22 = 1 / z_22
        h = np.array([[h_11, h_12], [h_21, h_22]])
    except:
        h = "Cannot find as z_22 = 0"

    try:
        t_11 = z_11 / z_21
        t_12 = delta_z / z_21
        t_21 = 1 / z_21
        t_22 = z_22 / z_21
        t = np.array([[t_11, t_12], [t_21, t_22]])
        a = complex(t_11)
        b = complex(t_12)
        c = complex(t_21)
        d = complex(t_22)
        image_parms(a, b, c, d)
    except:
        t = "Cannot find as z_21 = 0"

    print("\n Z TRANSFORM ")
    print(z)
    print("\n Y TRANSFORM ")
    print(y)
    print("\n H TRANSFORM ")
    print(h)
    print("\n T TRANSFORM ")
    print(t)

