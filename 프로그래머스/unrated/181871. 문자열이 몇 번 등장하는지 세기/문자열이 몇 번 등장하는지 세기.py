def solution(myString, pat):
    count = 0
    start = 0
    while start <= len(myString) - len(pat):
        idx = myString.find(pat, start)
        if idx != -1:
            count += 1
            start = idx + 1
        else:
            break
    return count
