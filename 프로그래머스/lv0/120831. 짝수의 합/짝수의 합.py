def solution(n):
    answer = 0
    even = 1
    
    while even <= n:
        if even % 2 == 0:
            answer += even
            even += 1
        else:
            even += 1
        
    return answer