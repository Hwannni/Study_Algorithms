# deque 이용하기
from collections import deque

def solution(N,number):
    # answer_deque로 deque 생성
    answer_deque = deque([(N,1)])
    while answer_deque:
        # popleft로 현재까지의 계산된 경우의 수와 N이 사용된 계수 출력
        current_cal, i = answer_deque.popleft()
        # 조건 1. i가 8초과면 -1 출력
        if i > 8 :
            return -1
        # 조건 2. current_cal이 number과 같다면 i 출력
        elif current_cal == number:
            return i
        # 모든조건에 거짓이라면 아래 실행
        else :
            answer_deque.append((current_cal + N,i+1))
            answer_deque.append((current_cal - N,i+1))
            answer_deque.append((current_cal * N,i+1))
            # 이쪽에서 문제가 생긴거 같은데..
            # ex) N은 5인데 current_cal이 10일때 105가 되므로 불
            answer_deque.append((int(str(current_cal) + str(N)),i+1))
            if current_cal != 0:
                answer_deque.append((current_cal // N,i+1))
        