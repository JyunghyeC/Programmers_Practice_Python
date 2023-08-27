def solution(arr, intervals):
    answer = []
    a1 = intervals[0][0]
    b1 = intervals[0][1] + 1
    
    a2 = intervals[1][0]
    b2 = intervals[1][1] + 1
    
    for i in range(a1, b1):
        answer.append(arr[i])
    
    for j in range(a2, b2):
        answer.append(arr[j])
    
    return answer