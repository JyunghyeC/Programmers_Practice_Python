def solution(myString, pat):
    return myString if myString.endswith(pat) else myString.rsplit(pat,1)[0] + pat