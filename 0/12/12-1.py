def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in my_string:
        for j in vowels:
            if i == j:
                my_string = my_string.replace(i, '')
    return my_string

# 또 다른 풀이
def solution2(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '')
    return my_string

def solution3(my_string):
    return ''.join([i for i in my_string if not (i in 'aeiou')])