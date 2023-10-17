def solution(rsp):
    answer = []
    for i in list(rsp):
        if i == '2':
            answer.append('0')
        elif i == '0':
            answer.append('5')
        else:
            answer.append('2')
    return ''.join(answer) # 문자열 -> 배열 -> 문자열 할 필요 X..

def solution2(rsp):
    answer = ''
    for i in rsp:
        if i == '0':
            answer += '5'
        elif i == '2':
            answer += '0'
        else:
            answer += '2'
    return answer

# 또 다른 풀이
def solution3(rsp):
    d = {'0':'5', '2':'0', '5':'2'}
    return ''.join(d[i] for i in rsp)

def solution4(rsp):
    rsp = rsp.replace('2','s')
    rsp = rsp.replace('s','0')
    rsp = rsp.replace('0','r')
    rsp = rsp.replace('r','5')
    rsp = rsp.replace('5','p')
    rsp = rsp.replace('p','2')
    return rsp