def solution(spell, dic):
    for c in dic:
        count = 0
        for s in spell:
            if s in c:
                count += 1
        if count == len(spell):
            return 1
    return 2


# 또 다른 풀이
def solution2(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell - set(s):
            return 1
    return 2