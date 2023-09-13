def solution(chicken):
    answer = -1
    coupon = 0
    remain = 0
    
    while chicken >= 10:
        coupon = chicken // 10
        remain = chicken % 10
        answer += coupon
        chicken = coupon + remain
            
    return answer + 1