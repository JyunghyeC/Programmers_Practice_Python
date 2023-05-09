def solution(num_str):
    answer = 0
    for i in num_str:
        if i.isdigit():
            answer += int(i)
    return answer