def solution(lines):
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))

    return len((s1 & s2) | (s2 & s3) | (s3 & s1))

# 또 다른 풀이
def solution2(lines):
    sets = [set(range(min(line), max(line))) for line in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])