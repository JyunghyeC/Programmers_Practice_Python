import re

def solution(myStr):
    answer = []
    for i in re.split('[a-c]', myStr):
        answer.append(i)
        
    return ["EMPTY"] if ' '.join(answer).split() == [] else ' '.join(answer).split()