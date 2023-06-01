def solution(num_list):
    mult = 1
    sqr = 0
    for i in num_list:
        mult *= i
        sqr += i
    
    if (sqr ** 2) > mult:
        return 1
    else:
        return 0