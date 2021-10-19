import numpy as np
from image_parameter import *

def t_to_other():
    a = complex(input("A= "))
    b = complex(input("B= "))
    c = complex(input("C= "))
    d = complex(input("D= "))

    delta_t_ = np.array([a])*np.array([d])-np.array([b])*np.array([c])
    delta_t = complex(delta_t_[0])

    t = np.array([[a, b], [c, d]])

    try:
        z_11 = a / c
        z_12 = delta_t / c
        z_21 = 1 / c
        z_22 = d / c
        z = np.array([[z_11, z_12], [z_21, z_22]])
    except:
        z = "Cannot find as c =0"

    try:
        y = np.linalg.inv(z)
    except:
        y = "Cannot find as delta_y =0"

    try:
        h_11 = b / d
        h_12 = delta_t / d
        h_21 = -1 / d
        h_22 = c / d
        h = np.array([[h_11, h_12], [h_21, h_22]])
    except:
        h = "Cannot find as d =0"

    print("\n Z TRANSFORM ")
    print(z)
    print("\n Y TRANSFORM ")
    print(y)
    print("\n H TRANSFORM ")
    print(h)
    print("\n T TRANSFORM ")
    print(t)
    image_parms(a, b, c, d)

