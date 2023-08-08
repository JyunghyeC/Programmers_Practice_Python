def solution(my_string, queries):
    lst = list(my_string)
    for i in queries:
        s, e = i
        lst[s:e + 1] = reversed(lst[s:e + 1])
        
    return ''.join(lst)