from collections import Counter
def solution(array):

    cnt = Counter(array)
    most = cnt.most_common()

    if len(cnt) == 1:
        return most[0][0]
    else:
        sec = most[0][1]
        third = most[1][1]
    
    if sec == third:
        return -1
    else:
        return most[0][0]
    
    