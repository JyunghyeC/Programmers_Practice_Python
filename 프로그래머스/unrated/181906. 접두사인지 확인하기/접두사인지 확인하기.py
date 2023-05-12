def solution(my_string, is_prefix):

    return 1 if is_prefix in my_string[0: len(is_prefix)] else 0