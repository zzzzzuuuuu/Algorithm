def solution(array, n):
    number = []
    array = sorted(array)
    for i in array:
        number.append(abs(i-n))
    return array[number.index(min(number))]

# 또 다른 풀이
def solution2(array, n):
    array.sort(key = lambda x: (abs(x-n), x-n))
    return array[0]