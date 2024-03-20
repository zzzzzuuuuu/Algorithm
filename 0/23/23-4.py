def solution(id_pw, db):
    for i in db:
        if id_pw[0] in i:
            return "login" if id_pw[1] in i else "wrong pw"
    return "fail"