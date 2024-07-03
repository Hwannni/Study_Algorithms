import heapq

def solution(scoville, K):
    # scoville리스트를 heapq를 사용하기위해 heapify 적용하기
    heapq.heapify(scoville)
    # 숫자를 세기위한 count변수 생성하기
    count = 0
    # 여러번 반복수행 해야하므로 while문 적용하기
    while True:
        # 제한사항 적용
        if len(scoville) == 0:
            return -1
        # scoville안에서 제일 작은 수 first_min에 담기
        first_min = heapq.heappop(scoville)
        # 조건 1. 만약 first_min이 K보다 크거나 같으면 count return
        if first_min >= K:
            return count
        # 조건 2. 조건 1에서 건너뛰고 scoville안에 아무것도 없으면 제한사항 적용
        elif len(scoville) == 0:
            return -1
        else:
            # 카운트 +1
            count += 1
            # ((first_min제외)) scoville안에서 제일 작은 수 second_min에 담기
            second_min = heapq.heappop(scoville)
            # 섞은 음식의 스코빌 지수 공식 적용
            mix_scoville = first_min + second_min * 2
            # scoville에 mix_scoville 추가하기
            heapq.heappush(scoville, mix_scoville)
