def solution(num_list):
    i = 0
    num_list.reverse()
    if num_list[0] > num_list[1]:
        i = num_list[0] - num_list[1]
        num_list.reverse()
        num_list.append(i)
    else:
        num_list.insert(0, num_list[0] * 2)
        num_list.reverse()
    return num_list
            