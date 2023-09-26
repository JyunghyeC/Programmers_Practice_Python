def solution(n):
    answer = []
    rev = ''
    for i in str(n):
        rev += i
    
    rev = int(rev)
    
    while rev >= 1:
        answer.append(rev % 10)
        rev //= 10
    return answer