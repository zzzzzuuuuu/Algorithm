def solution(n):
    answer = 0
    for i in range(n+1):
        if i%2 == 0:
            answer += i
    return answer

# 또 다른 풀이
def solution2(n):
    return sum(i for i in range(2, n+1, 2)) # range(start, stop, step)
