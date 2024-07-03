def solution(survey,choices):
    # 검사지표 리스트와 시키기
    mbti_lst = ["R","T","C","F","J","M","A","N"]
    # 빈 딕셔너리 만들기
    mbti_dic = {}
    # 점수 표기를 하기 위해 {"R":0} 형태로 만들기
    for mbti in mbti_lst:
        mbti_dic[mbti] = 0
    # survey와 choices는 길이가 같다.
    length = len(survey)
    # 조사지와 선택한걸 토대로 점수화 시키기
    for i in range(length):
        # choices[i]가 3보다 클때 점수
        if choices[i] > 4 :
            # 오른쪽에 알파벳이 점수 획득
            score = survey[i][1]
            mbti_dic[score] += choices[i] - 4
        # choices[i]가 3보다 작을때 점수
        elif choices[i] < 4 :
            # 왼쪽에 알파벳이 점수 획득
            score = survey[i][0]
            mbti_dic[score] += 4 - choices[i]
    # 정답을 위한 빈 문자열 생성
    answer = ""
    # 2개씩 mbti_lst를 돌면서 점수비교하기
    for check in range(0,8,2):
        # 2개를 담는 리스트 만들기
        compare = mbti_lst[check:check+2]
        # 점수가 같을 경우 앞에 알파벳 answer에 붙히기
        if mbti_dic[compare[0]] == mbti_dic[compare[1]]:
            answer += compare[0]
        # 점수가 큰쪽에 알파벳 answer에 붙히기
        elif mbti_dic[compare[0]] > mbti_dic[compare[1]]:
            answer += compare[0]
        elif mbti_dic[compare[0]] < mbti_dic[compare[1]]:
            answer += compare[1]
    return answer