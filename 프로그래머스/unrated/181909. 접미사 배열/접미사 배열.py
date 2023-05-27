def solution(my_string):
    answer = []
    cnt = -1
    for i in my_string:
        answer.append(my_string[cnt:])
        cnt -= 1
    answer.sort()
    return answer