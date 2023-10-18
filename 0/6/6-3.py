def solution(num_list):
    even = [] # 짝수
    odd = [] # 홀수
    for i in num_list:
        if i%2 == 0:
            even.append(i)
        else: odd.append(i)
    return [len(even), len(odd)]

# 또 다른 풀이 (1)
def solution(num_list):
    odd = sum(1 for n in num_list if n % 2)
    return [len(num_list) - odd, odd] # 짝수, 홀수 순서로 리턴

# 또 다른 풀이 (2)
def solution(num_list):
    answer = [0, 0]
    for n in num_list:
        answer[n%2] += 1
    return answer