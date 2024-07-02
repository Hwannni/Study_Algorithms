import heapq

def solution(k, score):
    # 명예의 전당 리스트 만들기
    awards_lst = []
    # 정답 리스트 만들기
    answer = []
    # score리스트로 for문 돌리기
    for s in score:
        # heapq을 이용하여 명예의 전당 리스트에 담아주기
        heapq.heappush(awards_lst, s)
        # 조건 1. 만약 명예의 전당에 길이가 k보다 크면 제일 작은 점수 제거하기
        if len(awards_lst) > k:
            heapq.heappop(awards_lst)
        # 현재 명예의 전당 리스트중 제일 작은 점수 정답리스트에 추가하기
        answer.append(awards_lst[0])
    return answer
