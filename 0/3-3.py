from collections import Counter

def solution(array):
    cnt = Counter(array)  # {'1': 1, '2': 1, '3': 3, '4': 1}
    max_count = max(cnt.values())  # 3
    result = []

    for k, v in cnt.items():
        if v == max_count:
            result.append(k)

    if len(result) == 1:
        return result[0]
    else:
        return -1
