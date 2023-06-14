def solution(myString):

    myString = myString.replace('a', 'A');
    lst = list(myString)
    for i in range(len(lst)):
        if lst[i] != 'A':
            lst[i] = lst[i].lower()
    
    return ''.join(lst)
