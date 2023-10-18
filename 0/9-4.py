import math
def solution(balls, share):
     return math.factorial(balls)/(math.factorial(balls-share)*math.factorial(share))

# 또 다른 풀이
import math
def solution2(balls, share):
    return math.comb(balls, share)

