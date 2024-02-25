def solution(my_string):
    alphabet = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e',
               'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j',
               'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o', 'P': 'p',
               'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u', 'V': 'v',
               'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'}
    for s in my_string:
        if s in alphabet.keys():
            my_string = my_string.replace(s, alphabet[s])
    return ''.join(sorted(my_string))

# 또 다른 풀이
def solution2(my_string):
    return ''.join(sorted(my_string.lower()))