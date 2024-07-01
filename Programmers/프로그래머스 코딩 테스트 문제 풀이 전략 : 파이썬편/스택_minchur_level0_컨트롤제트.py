def solution(s):
    # 정답에 쓸 변수 생성하기
    answer = 0
    # 문자열 s를 리스트화 시키기
    s_lst = s.split(" ")
    # s_lst의 길이로 for문 돌리기 
    for i in range(len(s_lst)):
        # Z가 있는지 검증하기
        if s_lst[i] == "Z":
            answer -= int(s_lst[i-1])
        # 아닌경우 더 해주기
        else :
            answer += int(s_lst[i])
    return answer
            