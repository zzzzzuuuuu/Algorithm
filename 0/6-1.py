def solution(my_string):
    my_list = list(my_string)
    result = []
    while(my_list):
        keeps = my_list.pop()
        result.append(keeps)
    return ''.join(result)

# 또 다른 풀이
def solution(my_string):
    return my_string[::-1] # 슬라이싱 사용->바로 역순으로 정렬