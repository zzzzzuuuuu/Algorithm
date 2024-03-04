def solution(polynomial):
    polynomial = polynomial.split(' + ')
    x, n = 0, 0
    for c in polynomial:
        if c.isdigit(): # 상수항
            n += int(c)
        else: # 일차항
            x = x + 1 if c == 'x' else x + int(c[:-1])
    if x == 0 or n == 0:
        if x == 0 and n != 0:
            return str(n)
        elif x != 0 and n == 0:
            return (str(x) + 'x') if x != 1 else str('x')
        else:
            return str('0')
    else:
        return (str(x) + 'x' + ' + ' + str(n)) if x != 1 else ('x' + ' + ' + str(n))

# 또 다른 풀이
def solution2(polynomial):
    x, n = 0, 0
    for c in polynomial.split(' + '):
        if c.isdigit():
            n += int(c)
        else:
            x = x + 1 if c == 'x' else x + int(c[:-1])
    if x == 0:
        return str(n)
    elif x == 1:
        return 'x + ' + str(n) if n != 0 else 'x'
    else:
        return f'{x}x + {n}' if n != 0 else f'{x}x'