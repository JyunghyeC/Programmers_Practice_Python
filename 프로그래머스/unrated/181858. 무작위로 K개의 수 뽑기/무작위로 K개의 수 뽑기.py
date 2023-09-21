def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer and len(answer) < k:
            answer.append(i)
    
    for j in answer:
        if len(answer) < k:
            answer.append(-1)
    return answer