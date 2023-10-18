def solution(num_list):
    num_list.reverse()
    return num_list

# 또 다른 풀이 (1)
def solution(num_list):
    return num_list[::-1] # 슬라이싱 역순으로 정렬

# 또 다른 풀이 (2)
def solution(num_list):
    result = []
    while(num_list):
        result.append(num_list.pop()) # 인자가 없으면 배열의 마지막 요소가 제거되고 반환
    return result
