def solution(score):
    answer = []
    aver = []
    for i in score:
        aver.append(sum(i) / 2)
    
    sort_aver = sorted(aver, reverse = True)
    
    for i in aver:
        answer.append(sort_aver.index(i) + 1)
    return answer