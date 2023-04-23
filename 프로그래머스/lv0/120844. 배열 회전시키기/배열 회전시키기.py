def solution(numbers, direction):

    if direction == 'right' :
        r = numbers[len(numbers) - 1]
        numbers.remove(r)
        numbers.insert(0, r)
    else :
        l = numbers[0]
        numbers.remove(l)
        numbers.append(l)
    return numbers