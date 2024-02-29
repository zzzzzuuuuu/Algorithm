def solution(array):
    count = 0
    for i in array:
        count += str(i).count('7')
    return count

# 또 다른 풀이
def solution2(array):
    return str(array).count('7')

def solution3(array):
    return ''.join(map(str, array)).count('7')