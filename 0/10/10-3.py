def solution(numbers, k):
    numbersList = []
    while k*2 >= len(numbersList):
        numbersList += numbers
    return numbersList[2*(k-1)] # k가 1부터 시작하는 인덱스로 간주하기 위해 -1

# 또 다른 풀이
def solution2(numbers, k):
    return numbers[2*(k-1) % len(numbers)] # 결과 인덱스(=2*(k-1))가 리스트의 길이보다 클 경우 리스트 길이로 나눠 나머지로 변환