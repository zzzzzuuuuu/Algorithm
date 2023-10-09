def solution(numbers):
    avg = 0
    for i in range(0, len(numbers)):
        avg += numbers[i]
    return avg / len(numbers)

# 또 다른 풀이
def solution(numbers):
    return sum(numbers) / len(numbers)