def solution(n):
    answer = 0
    x = 1
    
    while n >= 1:
        if n % x == 1:
            return x
        else:
            x += 1
    


