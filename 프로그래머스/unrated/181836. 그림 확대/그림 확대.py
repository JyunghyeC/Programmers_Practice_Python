def solution(picture, k):
    answer = []
    
    for i in picture:
        resized = ''
        for j in i:
            resized += j * k
        for num in range(k):
            answer.append(resized)
            
    return answer