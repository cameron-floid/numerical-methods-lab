"""

Errors:

Ea: Absolute error
Mv: Measured value
Av: Actual value
Er: Relative error

i.      Ea = |Mv - Av|
ii.     Er = Ea / Av
iii.    Er% = Er x 100

"""


"""
1. Find the absolute error and relative error of the approximation 125.67 to the value 119.66
"""


def find_ea(mv: float, av: float):

    ea = mv - av
    return abs(ea)


def find_er(ea: float, av: float):

    er = ea / av
    return er


mv = 125.67
av = 119.66

ea = find_ea(mv, av)
er = find_er(ea, av)

print(f"absolute error for values mv = {mv}, av = {av} => {ea}")
print(f"relative error for values ea = {ea}, av = {av} => {er}")
