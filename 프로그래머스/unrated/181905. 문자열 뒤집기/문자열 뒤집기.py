def solution(my_string, s, e):
    if s < 0 or e >= len(my_string) or s > e:
        return "Invalid index range"

    # s부터 e까지의 부분 문자열을 추출하고 뒤집기
    substring = my_string[s:e+1]
    reversed_substring = "".join(reversed(substring))

    # 뒤집은 부분 문자열을 my_string에 삽입
    answer = my_string[:s] + reversed_substring + my_string[e+1:]
    return answer