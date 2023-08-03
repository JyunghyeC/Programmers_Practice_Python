def solution(arr, queries):
    answer = []
    for i in queries:
        s, e = i
        for i in range(s, e + 1):
            arr[i] += 1
    return arr