from z_to_other import *
from y_to_other import *
from h_to_other import *
from t_to_other import *
from color import bcolors

print(f"\n{bcolors.BOLD}{bcolors.FAIL}Welcome to the 2_port_network parameter calculator by ALIAS GEORGE{bcolors.ENDC}\n")
print(f"{bcolors.OKCYAN}You can enter complex number in a+bj format {bcolors.ENDC}\n")
choice = input(f"Which parameter you have {bcolors.HEADER}z / y / h / t ?{bcolors.ENDC} ")

if choice == "z":
    z_to_other()

elif choice == "y":
    y_to_other()

elif choice == "h":
    h_to_other()

elif choice == "t":
    t_to_other()





