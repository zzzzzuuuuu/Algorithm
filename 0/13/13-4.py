def solution(sides):
    sides.sort()
    if sides[2] < sides[0] + sides[1]:
        return 1
    else:
        return 2

    # 또 다른 풀이
    def solution2(sides):
        sides.sort()
        return 1 if sides[0] + sides[1] > sides[2] else 2

    def solution3(sides):
        return 1 if max(sides) < (sum(sides) - max(sides)) else 2