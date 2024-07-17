def solution(score):
    avg_score = []
    ranks = []
    
    # 평균 점수 계산
    for i in score:
        avg_score.append(sum(i)/2)
        
    # 정렬
    sort_avg = sorted(avg_score, reverse = True)
    
    # 랭킹 출력
    for i in avg_score:
        ranks.append(sort_avg.index(i)+1)
    return ranks