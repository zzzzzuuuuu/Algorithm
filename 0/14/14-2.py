def solution(order):
    orderList = list(map(int, str(order)))
    count = 0
    for i in orderList:
        if i != 0:
            if i % 3 == 0:
                count += 1
    return count

# 또 다른 풀이
def solution2(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))

def solution3(order):
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')