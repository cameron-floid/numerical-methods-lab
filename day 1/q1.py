from math import sqrt


def formula_1(a: float, b: float, c: float):

    # find xp (x positive)
    xp = (-b + sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)

    # find xn (x negative)
    xn = (-b - sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)

    return xp, xn


def formula_2(a: float, b: float, c: float):

    # find xp (x positive)
    xp = 2 * c / (-b + sqrt(pow(b, 2) - 4 * a * c))

    # find xn (x negative)
    xn = 2 * c / (-b - sqrt(pow(b, 2) - 4 * a * c))

    return xp, xn


def find_ea(mv: float, av: float):
    ea = mv - av
    return abs(ea)


def find_er(ea: float, av: float):
    er = ea / av
    return er


"""
1. Find the absolute error and relative error for the values obtained from formula_1 and formula_2
"""

# Given values for the quadratic equation
a = 0.001
b = 1000
c = 0.001

# get the results from the two functions
actual_xp, actual_xn = formula_1(a, b, c)
measured_xp, measured_xn = formula_2(a, b, c)

# Calculate absolute and relative errors for xp
ea_xp = find_ea(measured_xp, actual_xp)
er_xp = find_er(ea_xp, actual_xp)

# Calculate absolute and relative errors for xn
ea_xn = find_ea(measured_xn, actual_xn)
er_xn = find_er(ea_xn, actual_xn)

# Print the results
print(f"For xp: absolute error = {ea_xp}, relative error = {er_xp}")
print(f"For xn: absolute error = {ea_xn}, relative error = {er_xn}")
