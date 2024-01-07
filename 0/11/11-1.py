def solution(box, n):
    answer = 1
    for i in range(len(box)):
        answer = answer * int(box[i]/n)
    return answer

# 또 다른 풀이
def solution2(box, n):
    a, b, c = box
    return (a//n) * (b//n) * (c//n)