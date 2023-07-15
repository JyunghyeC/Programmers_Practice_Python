def solution(myString):
    answer = []
    lst = []
    
    answer = myString.split("x")
    for i in answer:
        lst.append(len(i))
        
    return lst