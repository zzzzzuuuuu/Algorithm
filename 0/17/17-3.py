def solution(n):
    return sum(list(map(int, str(n))))
# list() 쓸 필요 X

# 또 다른 풀이
def solution2(n):
	return sum(int(i) for i in str(n))