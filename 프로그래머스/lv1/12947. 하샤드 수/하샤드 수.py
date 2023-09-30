def solution(x):
    num = []
    
    for i in str(x):
        num.append(int(i))
        
    if x % sum(num) == 0:
        return True
    else:
        return False
