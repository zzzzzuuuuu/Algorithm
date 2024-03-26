def solution(score):
    avg = [sum(s)/len(s) for s in score]
    sorted_avg = sorted(avg, reverse=True)
    grade = []
    for s in avg:
        grade.append(sorted_avg.index(s) + 1)
    return grade

def solution2(score):
    a = sorted([sum(i) for i in score], reverse=True)
    return [a.index(sum(i))+1 for i in score]