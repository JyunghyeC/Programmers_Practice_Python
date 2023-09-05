def solution(A, B):

    cnt = -1
    

    if A == B:
        return 0
    
    for i in range(1, len(A)):
            A = A[-1] + A[:-1]
            if A == B:
                return i
        
    
    return cnt
            
