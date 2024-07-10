def solution(s):
    # 문자 카운팅을 위한 딕셔너리 만들기
    count_dic = {}
    # 정답에 담을 리스트 만들기
    answer = []
    # s로 for문 돌리기
    for i in range(len(s)):
        # 만약 s[i]가 count_dic안에 없으면 추가
        if s[i] not in count_dic:
            count_dic[s[i]] = i
            answer.append(-1)
        # 있다면 인덱스 차이를 answer에 담아주기
        else :
            answer_bet = i - count_dic[s[i]]
            count_dic[s[i]] = i
            answer.append(answer_bet)
    return answer
            