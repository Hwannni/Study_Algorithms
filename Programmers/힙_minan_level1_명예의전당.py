import heapq

def solution(k, score):
    ranking = []
    result = []
    
    for i in score:
        # 명예의 전당의 크기 조건
        if len(ranking) < k:
            # 힙푸쉬를 이용하여 heap에 score 담기
            heapq.heappush(ranking, i)
        else:
            # 힙푸쉬팝을 이용하여 랭킹의 점수를 추가하며, 최하점은 pop!
            if i > ranking[0]:
                heapq.heappushpop(ranking, i)
                
        # 매일 ranking 최하위 점수를 result에 추가
        result.append(ranking[0])
        
    return result