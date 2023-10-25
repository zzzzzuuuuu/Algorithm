def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]

# 또 다른 풀이
def solution2(numbers):
    numbers.sort()
    return numbers[-1]*numbers[-2]