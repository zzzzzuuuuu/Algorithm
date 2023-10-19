def solution(numbers, direction):
    keeps = 0
    if direction == 'right':
        keeps = numbers.pop()
        numbers.insert(0, keeps) # 변수 keeps에 저장하지 않고 바로 쓰는 것도.. 됨
    else:
        keeps = numbers.pop(0)
        numbers.append(keeps)
    return numbers

# 또 다른 풀이
from collections import deque
def solution2(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)

def solution3(numbers, direction):
    return [numbers[-1] + numbers[:-1] if direction == 'right' else numbers[1:] + numbers[0]]