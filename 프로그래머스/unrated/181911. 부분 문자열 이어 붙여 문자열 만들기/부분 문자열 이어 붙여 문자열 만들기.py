def solution(my_strings, parts):
    answer = ''
    letters = ''
    for i in range(0, len(my_strings)):
        letters = my_strings[i]
        
        answer += letters[parts[i][0] : parts[i][1] + 1]
        
    return answer