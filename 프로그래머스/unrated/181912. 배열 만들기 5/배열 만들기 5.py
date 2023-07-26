def solution(intStrs, k, s, l):
    answer = []
    tmp = ""

    for i in range(len(intStrs)):
        tmp = intStrs[i]
        if int(tmp[s : s + l]) > k:
            answer.append(int(tmp[s : s + l]))
    return answer