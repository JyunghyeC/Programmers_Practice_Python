def solution(id_pw, db):

    for i in db:
        if id_pw[0] == i[0]:
            if i[1] == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
    
    return "fail"