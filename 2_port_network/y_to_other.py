import numpy as np
from image_parameter import *


def y_to_other():
    y_11 = complex(input("y_11= "))
    y_12 = complex(input("y_12= "))
    y_21 = complex(input("y_21= "))
    y_22 = complex(input("y_22= "))

    delta_y_ = np.array([y_11])*np.array([y_22])-np.array([y_12])*np.array([y_21])
    delta_y = complex(delta_y_[0])

    y = np.array([[y_11, y_12], [y_21, y_22]])
    try:
        z = np.linalg.inv(y)

    except:
        z = "Cannot find as delta_y =0"
    try:
        h_11 = 1 / y_11
        h_12 = -y_12 / y_11
        h_21 = y_21 / y_11
        h_22 = delta_y / y_11
        h = np.array([[h_11, h_12], [h_21, h_22]])
    except:
        h = "Cannot find as y_11 =0"

    try:
        t_11 = -y_22 / y_21
        t_12 = -1 / y_21
        t_21 = -delta_y / y_21
        t_22 = -y_11 / y_21
        t = np.array([[t_11, t_12], [t_21, t_22]])
        a = complex(t_11)
        b = complex(t_12)
        c = complex(t_21)
        d = complex(t_22)
        image_parms(a, b, c, d)
    except:
        t = "Cannot find as y_21 =0"

    print("\n Z TRANSFORM ")
    print(z)
    print("\n Y TRANSFORM ")
    print(y)
    print("\n H TRANSFORM ")
    print(h)
    print("\n T TRANSFORM ")
    print(t)

