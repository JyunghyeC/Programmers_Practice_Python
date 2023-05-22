def solution(myString, pat):
    answer = ""
    newPat = ""
    for i in pat:
        if i == "A":
            newPat += "B" 
        else:
            newPat += "A"
    
    return 1 if newPat in myString else 0