def solution(s):
    answer = 0
    str = s.split()
    for i in range(len(str)):
        if str[i] == "Z":
            answer -= int(str[i-1])
        else:
            answer += int(str[i])
    return answer