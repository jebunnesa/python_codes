# import math
#
# ab = 10
# bc = 10
#
# mc = math.sqrt(ab*ab + bc*bc)/2
# angle_val = round(math.degrees(math.acos((bc*bc) / (2*mc*bc))))
#
# print(f"{angle_val}°")

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x,y : x*y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)