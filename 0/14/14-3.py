def solution(cipher, code):
    cipherList = list(map(str, cipher))
    answer = ''
    for i in range(1, len(cipherList) // code + 1):
        answer += cipherList[code * i - 1]
    return answer
