def solution(phone_number):
    backNum = phone_number[-4:]
    return '*' * len(phone_number[:-4]) + backNum