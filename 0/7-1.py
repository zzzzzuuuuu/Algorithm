def solution(my_string, letter):
    my_list = list(my_string)
    my_list = [i for i in my_list if i != letter]
    return ''.join(my_list)
    # string에서도 for문 사용이 가능 & 리스트 컴프리헨션으로 코드 간결화 가능
    # return ''.join([i for i in my_string if i != letter])

# 또 다른 코드
def solution2(my_string, letter):
    return my_string.replace(letter, '')
