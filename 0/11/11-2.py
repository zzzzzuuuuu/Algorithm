def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True


def solution(n):
    prime = 1
    for i in range(n + 1):
        if isPrime(i) == True:
            prime += 1
    return n - prime

# 또 다른 풀이 -> n 제곱근 이용: n의 약수는 무조건 n의 제곱근 범위에 존재함

def solution2(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output