def solution(numbers, n):
    summ = 0
    for i in list(numbers):
        summ += i
        if summ > n :
            return summ
        else:
            continue
        