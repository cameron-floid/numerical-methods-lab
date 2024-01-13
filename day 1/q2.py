from math import sqrt
from q1 import find_ea, find_er


"""
consider the quadratic equation of the curve ax^2 + bx + c = 0 whose values can be calculated using the formula:

x = ( -b +/- sqrt(b^2 - 4*a*c) ) / 2a

Alternatively we can re-write the above formula as:

x = 2c / ( -b +/- sqrt(b^2 - 4*a*c) )

for the values:

a = 0.001
b = 1000
c = 0.001

how can we use the expressions to get the accurate values

"""


def formula_1(a: float, b: float, c: float):

    xp = (-b + sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)
    xn = (-b - sqrt(pow(b, 2) - 4 * a * c)) / (2 * a)

    return xp, xn


def formula_2(a: float, b: float, c: float):

    xp = (2 * c) / (-b + sqrt(pow(b, 2) - 4 * a * c))
    xn = (2 * c) / (-b - sqrt(pow(b, 2) - 4 * a * c))

    return xp, xn


a = 0.001
b = 1000
c = 0.001


avx, avy = formula_1(a, b, c)
mvx, mvy = formula_2(a, b, c)


"""
Compute the absolute and relative error
"""

eax = find_ea(mvx, avx)
eay = find_ea(mvy, avy)

erx = find_er(mvx, avx)
ery = find_er(mvy, avy)


print(f"x ea => {eax}, y ea => {eay}")
print(f"x er => {erx}, y er => {ery}")
