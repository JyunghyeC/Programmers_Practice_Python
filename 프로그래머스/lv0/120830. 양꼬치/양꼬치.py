def solution(n, k):
    lamb = n * 12000
    drink = k * 2000
    service = (n // 10) * 2000
    
    return (lamb + drink) - service