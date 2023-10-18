def solution(hp):
    # ants = {'J': 5, 'B': 3, 'I': 1}
    # return hp//ants['J'] + (hp%ants['J'])//ants['B'] + hp%ants['J']%ants['B'] # 사전으로 굳이 할 필요가...
    return hp//5 + hp%5//3 + hp%5%3

# 또 다른 풀이
def solution2(hp):
    answer = 0
    for ants in [5, 3, 1]:
        d, hp = divmod(hp, ants)
        answer += d
    return answer