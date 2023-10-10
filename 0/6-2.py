n = int(input())
for i in range(1, n+1):
    print('*'*i)

# 또 다른 풀이
print('\n'.join('*' * (i + 1) for i in range(int(input())))) # 줄바꿈('\n') 단위로 출력