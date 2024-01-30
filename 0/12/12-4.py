def solution(n):
    prime = []
    i = 2
    while i <= n:
        if n % i == 0:
            if i not in prime:
                prime.append(i)
            n = n / i
        else:
            i = i + 1
    return prime