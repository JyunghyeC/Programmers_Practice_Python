def solution(a, b):
    num1 = str(a) + str(b)
    mult = 2 * a * b
    return max(int(num1), mult)