def solution(numLog):
    initialNumber = 0
    result = []

    for i in range(len(numLog)):
        diff = numLog[i] - initialNumber
        if diff == 1:
            result.append('w')
        elif diff == -1:
            result.append('s')
        elif diff == 10:
            result.append('d')
        elif diff == -10:
            result.append('a')
        initialNumber = numLog[i]

    return ''.join(result)