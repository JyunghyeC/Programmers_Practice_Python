def solution(myString):
    before = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    for i in myString:
        if i in before:
            myString = myString.replace(i, "l")  
    return myString
