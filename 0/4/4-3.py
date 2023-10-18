def solution(slice, n): # 피자 조각 수 slice(2~10), 사람 수 n
    return (n-1)//slice + 1

# 또 다른 풀이
def solution(slice, n):
    d, m = divmod(n, slice)
    return d + int(m != 0) # 나머지가 0이 아니면 +1