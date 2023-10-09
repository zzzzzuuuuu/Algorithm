def solution(n):
    answer = []
    for i in range(1, 100):
        if n * i % 6 == 0:
            answer.append(n*i//6)
            return answer[0]

# 또 다른 풀이
def solution(n):
    i=1
    while(1):
        if (6*i)%n==0:
            return i
        i+=1

def solution(n):
    answer = 1
    while 6 * answer % n:
        answer += 1
    return answer