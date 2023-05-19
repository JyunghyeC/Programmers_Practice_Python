def solution(my_string, alp):

    lst = list(my_string)
    for i in range(0, len(my_string)):
        if lst[i] == alp:
            lst[i] = lst[i].upper()
    return ''.join(lst)