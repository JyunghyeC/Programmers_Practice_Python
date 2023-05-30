def solution(binomial):

    lst = list(binomial.split(" "))
    if lst[1] == "+":
        return int(lst[0]) + int(lst[2])
    elif lst[1] == "-":
        return int(lst[0]) - int(lst[2])
    else:
        return int(lst[0]) * int(lst[2])
        