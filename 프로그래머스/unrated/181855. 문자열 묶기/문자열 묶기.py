def solution(strArr):
    count = {}
    for i in strArr:
        length = len(i)
        count[length] = count.get(length, 0) + 1
    return max(count.values())