def solution(num_list, n):
    answer = []
    c = 0
    for i in range(len(num_list)//n):
        answer.append([])
        while len(answer[i]) != n:
            answer[i].append(num_list[c])
            c += 1
    return answer

# 또 다른 풀이
def solution2(num_list, n):
    answer = []
    temp = [] # 임시 저장소
    for i in num_list:
        temp.append(i)
        if len(temp) == n:
            answer.append(temp)
            temp = []
    return answer

def solution3(num_list, n):
    answer = []
    for i in range(0, len(num_list), n): # n씩 증량
        answer.append(num_list[i:i+n])
    return answer