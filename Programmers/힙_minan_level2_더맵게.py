import heapq
import queue

def solution(scoville, K):
    answer = 0
    
    # 우선순위 큐 생성
    PQ_scoville = queue.PriorityQueue()
    
    # 모든 스코빌 지수를 우선순위 큐에 넣기
    for i in scoville:
        PQ_scoville.put(i)
    
    
    # 우선순위 큐의 사이즈가 1보다 커야함
    while PQ_scoville.qsize() > 1:
        # 가장 작은 스코빌과 그 다음으로 작은 스코빌 get
        min_scov = PQ_scoville.get()
        sec_scov = PQ_scoville.get()
        # mix_scov 정의
        mix_scov = min_scov + (sec_scov * 2)
        
        # mix_scov을 우선순위 큐에 넣기
        PQ_scoville.put(mix_scov)
        
        # 믹스한 횟수 만큼 answer도 1씩 증가
        answer += 1
        
    
        if PQ_scoville.queue[0] >= K:
            return answer
    


# def solution(scoville, K):
#     answer = 0
    
#     # 주어진 리스트 scoville을 먼저 힙구조로 변경! (heapify 함수)
#     heapq.heapify(scoville)
    
#     while len(scoville) > 1:
#         # 최저 스코빌이 K(기준치) 이상이라면 answer을 리턴하며 while문 종료!
#         if scoville[0] >= K:
#             return answer
        
#         # 가장 작은 두 개의 스코빌 지수를 힙팝
#         min1 = heapq.heappop(scoville)
#         min2 = heapq.heappop(scoville)
        
#         # 섞은 결과를 다시 힙에 추가
#         # 문제에서 주어진 식 사용
#         mix_scoville = min1 + (min2 * 2)
#         heapq.heappush(scoville, mix_scoville)
        
#         # mix_scoville 횟수에 따라 answer도 1씩 증가
#         answer += 1
        
#     return answer