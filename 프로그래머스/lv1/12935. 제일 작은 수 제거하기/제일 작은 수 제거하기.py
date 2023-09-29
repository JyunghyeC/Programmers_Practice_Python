def solution(arr):
    answer = []
    lowest = min(arr)
    
    for i in arr:
        if i != lowest:
            answer.append(i)
            
    return answer if len(answer) > 1 else [-1]