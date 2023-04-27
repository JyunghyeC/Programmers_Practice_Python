def solution(i, j, k):
    answer = 0
    for l in range(i, j + 1):
        if str(k) in str(l) and str(k) in str(l):
            answer += int(str(l).count(str(k)))
    return answer