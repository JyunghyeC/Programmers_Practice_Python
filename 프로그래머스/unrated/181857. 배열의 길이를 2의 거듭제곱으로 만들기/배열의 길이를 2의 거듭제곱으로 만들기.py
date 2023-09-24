def solution(arr):
    i = 0
    length = len(arr)
    
    while length > 1:
        length /= 2
        i += 1
    
    return arr + [0] * (2 ** i - len(arr))
        
        
        