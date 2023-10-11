def solution(angle):
    if angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    else: return 4

    # 또 다른 풀이
    def solution2(angle):
        if angle <= 90:
            return 1 if angle < 90 else 2
        else:
            return 3 if angle < 180 else 4
