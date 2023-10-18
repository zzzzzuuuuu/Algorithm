def solution(dot):
    if dot[0] > 0:
        return (1 if dot[1] > 0 else 4)
    else:
        return (3 if dot[1] < 0 else 2)

# 또 다른 풀이
def solution2(dot):
    quad = [(3,2), (4,1)] # [0][0] [0][1] [1][0] [1][1]
    return quad[dot[0] > 0][dot[1] > 0]