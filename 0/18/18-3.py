def solution(n, t):
    result = n
    for i in range(t):
        result = result * 2
    return result

# 또 다른 풀이
def solution2(n, t):
	return n * 2 ** t

def solution3(n, t):
	return n << t