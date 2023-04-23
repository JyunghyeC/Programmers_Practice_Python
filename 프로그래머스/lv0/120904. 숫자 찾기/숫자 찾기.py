def solution(num, k):
    numbers = str(num)
    i = str(k)
    
    if i in numbers :
        return numbers.index(i) + 1
    else :
        return -1
