def solution(sides):
    sides.sort()
    result = 0

    for i in range(1, sides[1] + 1):
        if i > sides[1] - sides[0]:
            result += 1

    for i in range(sides[1] + 1, sum(sides)):
        result += 1

    return result

# 또 다른 풀이
def solution2(sides):
    return sum(sides) - max(sides) + min(sides) - 1