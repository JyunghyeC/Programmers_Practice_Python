def solution(s):
    cntP = 0
    cntY = 0
    
    for i in s:
        if i == "P" or i == "p":
            cntP += 1
        elif i == "Y" or i == "y":
            cntY += 1
        else:
            continue
    
    return True if cntP == cntY else False