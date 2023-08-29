def solution(arr):
    first = -1
    last = -1
    
    for i in range(len(arr)):
        if arr[i] == 2:
            if first == -1:
                first = i   
            else:
                last = i
    
    if first == -1:
        return [-1]
    elif last == -1:
        return [2]
    
    return arr[first:last + 1] 