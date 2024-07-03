def solution(my_string):
    # my_string 리스트화 시키기
    my_lst = list(my_string)
    # 정답에 쓸 빈 문자열 생성하기
    answer = ""
    # my_lst로 for문 돌리기
    for i in my_lst :
        # 검증 1. i가 answer에 있는지 확인
        if i not in answer:
            # 없다면 answer에 추가해주기
            answer += i
    return answer