def solution(my_string):
    numbers = []
    for i in my_string:
        if i.isdigit():
            numbers.append(int(i))
    return sorted(numbers)

# 또 다른 풀이
def solution2(my_string):
    return sorted([int(i) for i in my_string if i.isdigit()])

def solution3(my_string):
    return sorted(map(int, filter(lambda x: x.isdigit(), my_string)))