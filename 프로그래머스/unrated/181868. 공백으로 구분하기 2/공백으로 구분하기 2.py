def solution(my_string):
    answer = []
    lst = my_string.split(' ')
    return [word for word in lst if word != '']
