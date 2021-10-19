import numpy as np
from image_parameter import *


def h_to_other():
    h_11 = complex(input("h_11= "))
    h_12 = complex(input("h_12= "))
    h_21 = complex(input("h_21= "))
    h_22 = complex(input("h_22= "))

    delta_h_ = np.array([h_11])*np.array([h_22])-np.array([h_12])*np.array([h_21])
    delta_h = complex(delta_h_[0])

    h = np.array([[h_11, h_12], [h_21, h_22]])
    try:
        z_11 = delta_h / h_22
        z_12 = h_12 / h_22
        z_21 = -h_21 / h_22
        z_22 = 1 / h_22
        z = np.array([[z_11, z_12], [z_21, z_22]])
    except:
        z = "Cannot find as h_22 =0"

    try:
        y = np.linalg.inv(z)
    except:
        y = "Cannot find as delta_y =0"

    try:
        t_11 = -delta_h / h_21
        t_12 = -h_11 / h_21
        t_21 = -h_22 / h_21
        t_22 = -1 / h_21
        t = np.array([[t_11, t_12], [t_21, t_22]])
        a = complex(t_11)
        b = complex(t_12)
        c = complex(t_21)
        d = complex(t_22)
        image_parms(a, b, c, d)
    except:
        t = "Cannot find as h_21 =0"

    print("\n Z TRANSFORM ")
    print(z)
    print("\n Y TRANSFORM ")
    print(y)
    print("\n H TRANSFORM ")
    print(h)
    print("\n T TRANSFORM ")
    print(t)

