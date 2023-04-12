def solution(numbers):
    answer = 0
    sum1 = 0
    
    for i in numbers:
        sum1 += i
        answer = sum1 / len(numbers)
    return answer