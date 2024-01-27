def solution(s):
    s_list = list(s.split())
    answer = []
    for i in range(len(s_list)):
        if s_list[i] == 'Z':
            answer.pop()
        else:
            answer.append(int(s_list[i]))
    return sum(answer)