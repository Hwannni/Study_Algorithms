def solution(score):
    # 평균점수를 담을 리스트 
    m_score = []
    # 평균점수 구하기
    for i in score:
        m = sum(i) / 2
        m_score.append(m)
    
    # 점수별 등수를 담아낼 딕셔너리 생성하기
    rank_dic = dict()
    _m_score = m_score.copy()
    for rank in range(1,len(_m_score)+1):
        # 최고 평균점수 변수에 담기
        m_max = max(_m_score)
        # m_score에서 제거하기
        _m_score.remove(m_max)
        # 딕셔너리에 담기
        if m_max not in rank_dic :
            rank_dic[m_max] = rank
    
    # answer list 생성하기
    answer = []
    # 순서대로 등수를 담아주기
    for s in m_score :
        answer.append(rank_dic[s])
    return answer
        