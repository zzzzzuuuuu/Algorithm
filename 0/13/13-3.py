def solution(my_string):
    my_list = []
    for i in my_string:
        if i not in my_list:
            my_list.append(i)
    return ''.join(my_list)

# 또 다른 풀이
def solution2(my_string): # 배열로 변환하지 않고 string 내에서 해결
    answer = ''
    for i in my_string:
        if i not in answer:
            answer += i
    return answer

def solution3(my_string): # my_string 값들을 딕셔너리 키로 만들어서 중복 제거
    return ''.join(dict.fromkeys(my_string))