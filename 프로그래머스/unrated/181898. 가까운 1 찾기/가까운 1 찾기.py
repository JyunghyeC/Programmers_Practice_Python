def solution(arr, idx):
    for i in range(0, len(arr)):
        if i >= idx and arr[i] == 1:
            return i
    return -1
        
