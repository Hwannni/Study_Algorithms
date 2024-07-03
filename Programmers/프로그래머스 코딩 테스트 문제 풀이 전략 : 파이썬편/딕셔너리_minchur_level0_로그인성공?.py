def solution(id_pw,db):
    # db for 문 돌리기
    for login in db :
        # ID 일치하는지 검증
        if id_pw[0] == login[0]:
            # PW 일치하는지 검증
            if id_pw[1] == login[1]:
                # ID,PW 둘다 일치하면 "login" 리턴
                return "login"
            else :
                # ID는 일치 하나 PW가 일치하지 않으므로 "wrong pw"리턴
                return "wrong pw"
    # ID조차 일치 하지 않으므로 "fail" 리턴
    return "fail"