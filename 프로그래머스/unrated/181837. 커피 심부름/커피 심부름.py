def solution(order):
    answer = []
    for i in range(len(order)):
        if "cafelatte" in order[i]:
            answer.append(5000)
        else:
            answer.append(4500)
            
    return sum(answer)