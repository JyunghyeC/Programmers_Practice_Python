def solution(numbers):

    numbers.sort()
    num1 = numbers[0] * numbers[1]
    num2 = numbers[len(numbers) - 1] * numbers[len(numbers) - 2]
    if num1 < num2 :
        return num2
    else :
        return num1