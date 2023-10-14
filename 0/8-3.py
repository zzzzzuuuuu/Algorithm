def solution(emergency):
    count = 1
    n = 0
    my_dict = {}
    for i in emergency:
        my_dict[i] = ''

    while emergency:
        n = max(emergency)
        my_dict[n] = count
        count += 1
        emergency.remove(n)
    return list(my_dict.values())

# 또 다른 풀이
def solution2(emergency):
    sort = sorted(emergency, reverse=True) # 내림차순. 긴급도가 높은 것부터 정렬
    return [sort.index(i)+1 for i in emergency] # sort 리스트에서 각 요소(i)가 처음 등장하는 인덱스(index)를 찾고 +1씩 해서 반환

def solution3(emergency):
    answer = []
    sort_num = sorted(emergency, reverse = True)

    for i in emergency:
        answer.append(sort_num.index(i) + 1)

    return answer