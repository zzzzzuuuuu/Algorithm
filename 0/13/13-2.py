def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

# 또 다른 풀이
def solution2(strlist):
    return [len(i) for i in strlist]

def solution3(strlist):
    return list(map(len, strlist))