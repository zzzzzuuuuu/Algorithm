def solution(quiz):
    answer = []
    for i in quiz:
        i = i.replace('=', '==')
        if eval(i) == True:
            answer.append('O')
        else:
            answer.append('X')
    return answer

# eval() 없이 다시 푼 코드
def solution2(quiz):
    answer = []
    for q in quiz:
        s, r = q.split(' = ')
        a, op, b = s.split(' ')
        if op == '+':
            if int(a) + int(b) == int(r):
                answer.append('O')
            else:
                answer.append('X')
        elif op == '-':
            if int(a) - int(b) == int(r):
                answer.append('O')
            else:
                answer.append('X')
    return answer