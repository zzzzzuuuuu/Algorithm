def solution(numbers):
    number_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
    number_keys = list(number_dict.keys())
    for i in number_keys:
        numbers = numbers.replace(i, number_dict[i])
    return int(numbers)

# 또 다른 풀이
def solution2(numbers):
    number_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
    for i in number_dict.keys(): # key를 배열에 저장하지 않고 바로 불러올 수 있음
        numbers = numbers.replace(i, number_dict[i])
    return int(numbers)

def solution3(numbers):
    for num, eng in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)