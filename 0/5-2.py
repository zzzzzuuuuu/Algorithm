def solution(money):
    n, r = divmod(money, 5500)
    return [n, r]