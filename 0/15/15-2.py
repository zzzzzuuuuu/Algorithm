def solution(my_string, num1, num2):
    my_list = list(my_string)
    result = []
    for i in range(len(my_list)):
        if i == num1:
            result.append(my_list[num2])
        elif i == num2:
            result.append(my_list[num1])
        else:
            result.append(my_list[i])
    return ''.join(result)

# 또 다른 풀이
def solution2(my_string, num1, num2):
    s = list(my_string)
    s[num1], s[num2] = s[num2], s[num1]
    return ''.join(s)