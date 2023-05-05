def solution(n):
    prime = []
    answer = []
    i = 2
    while i <= n :
        if n % i == 0 :
            prime.append(i)
            n = n // i
        else :
            i += 1
            
    for i in prime:
        if i not in answer:
            answer.append(i)
            
    return answer