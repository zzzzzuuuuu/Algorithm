def solution(my_string, n):
    result = []
    for i in list(my_string):
        for j in range(0, n):
            result.append(i)
    return ''.join(result) # 리스트로 하지 않고 빈 스트링에 저장해서 바로 리턴하는 쪽으로 고치기

# 또 다른 풀이
def solution2(my_string, n):
    return ''.join(i*n for i in my_string) # 리스트 컴프리헨션이므로 여기서 my_string의 타입은 리스트

def solution3(my_string, n):
    answer = ''
    for i in my_string: # for문에서 시퀀스로 string을 사용할 수 있으므로 배열로 변환하지 않아도 됨
        answer += i*n
    return answer