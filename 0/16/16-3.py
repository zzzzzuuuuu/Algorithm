def solution(my_string):
    my_list = my_string.split()
    result = int(my_list[0])
    for i in range(1, len(my_list), 2):
        if my_list[i]=='+':
            result += int(my_list[i+1])
        else:
            result -= int(my_list[i+1])
    return result

# 또 다른 풀이
def solution2(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))

def solution3(my_string):
    return eval(my_string)