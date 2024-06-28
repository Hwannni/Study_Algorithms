def solution(id_pw, db):
    
    # 주어진 id_pw를 딕셔너리로 변환
    dic = {'id':id_pw[0], 'pw':id_pw[1]}
    
    # 딕셔너리와 db 비교 
    # 즉, 이차원 배열의 요소가 딕셔너리의 값과 일치하는지 확인
    # db는 2차원 배열이므로 for문을 이용해서 전체를 확인해야함
    for i in db:
        # 만약 id와 pw 모두 일치한다면
        if i[0] == dic['id'] and i[1] == dic['pw']:
            return "login"
        # 만약 id는 일치하지만 pw는 일치하지 않는다면
        elif i[0] == dic["id"] and i[1] != dic['pw']:
            return "wrong pw"
    # 위 조건에 모두 부합하지 않는다면 결국 "fail"을 리턴!
    return "fail"
    