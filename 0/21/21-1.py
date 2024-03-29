def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())

# 또 다른 풀이
import re

def solution2(my_string):
    return sum([int(i) for i in re.findall(r'[0-9]+', my_string)])