def solution(id_pw, db):
    for i in db:
        if id_pw[0] in i:
            return "login" if id_pw[1] in i else "wrong pw"
    return "fail"


# 또 다른 풀이
def solution2(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]): # db를 사전으로 바꾼 뒤 해당 아이디(키)의 비밀번호(밸류)를 db_pw라는 변수에 할당, 없으면 none
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"