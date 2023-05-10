def solution(num_list):
    answer = 1
    if len(num_list) > 10 :
        return sum(i for i in num_list)
    else:
        for i in num_list:
            answer *= i
    return answer