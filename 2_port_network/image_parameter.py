import cmath
from color import bcolors


def image_parms(a, b, c, d):
    if a == d and (a * d - b * c).real - 1 < 0.01:
        print(f"\n{bcolors.WARNING}System is Reciprocal and Symmetric")
        try:
            z_0 = cmath.sqrt(b / c)
        except:
            z_0 = "Cannot find b/c as c=0"
        e_gamma = a + cmath.sqrt(b * c)
        print(
            f"characteristic impedance z_0 = +-{z_0} and transfer constant e^gamma = {e_gamma} ")

    elif (a * d - b * c).real - 1 < 0.01:
        print(f"\n{bcolors.WARNING}System is Reciprocal")
        try:
            z_img_1 = cmath.sqrt((a * b) / (c * d))
        except:
            z_img_1 = "Cannot find as c or d is 0"
        try:
            z_img_2 = cmath.sqrt((d * b) / (c * a))
        except:
            z_img_2 = "Cannot find as c or a is 0"
        e_gamma = cmath.sqrt(a * d) + cmath.sqrt(b * c)
        print(
            f"z_img_1 = +- {z_img_1} and z_img_2 = +- {z_img_2} and transfer constant e^gamma = +- {e_gamma.real} ")

    elif a == d:
        print(f"{bcolors.WARNING}System is Symmetric")

    print(f"{bcolors.ENDC}")
