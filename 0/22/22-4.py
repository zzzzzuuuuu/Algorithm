from fractions import Fraction

def solution(a, b):
    n = Fraction(a,b)
    while n.denominator % 2 == 0:
        n = Fraction(n.numerator, n.denominator // 2)
    while n.denominator % 5 == 0:
        n = Fraction(n.numerator, n.denominator // 5)
    return 1 if n.denominator == 1 else 2

# 또 다른 풀이
from math import gcd

def solution2(a, b):
    b //= gcd(a, b)
    while b % 2 == 0:
        b //= 2
    while b % 5 == 0:
        b //= 5
    return 1 if b == 1 else 2