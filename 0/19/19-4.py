def solution(array, height):
    return len([i for i in array if i > height])

# 또 다른 풀이
def solution2(array, height):
    return sum(1 for i in array if i > height)