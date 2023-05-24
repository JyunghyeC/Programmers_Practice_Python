def solution(arr):
    answer = []
    j = 0
    for i in arr:
        j = i
        while j > 0:
            answer.append(i)
            j -= 1
    return answer