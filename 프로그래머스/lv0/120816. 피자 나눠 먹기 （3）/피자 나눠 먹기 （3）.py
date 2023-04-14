def solution(slice, n):
    
    if n % slice == 0 or n == slice:
        return n // slice
    else:
        return (n // slice) + 1