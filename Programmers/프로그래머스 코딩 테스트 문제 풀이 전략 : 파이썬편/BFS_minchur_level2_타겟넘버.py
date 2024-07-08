# deque 이용하기
from collections import deque

def solution(numbers, target):
    # 정답에 쓸 변수 설정
    answer = 0
    # answer_deque로 deque 생성
    answer_deque = deque([(0, 0)]) 
    
    while answer_deque:
        # popleft로 현재까지 계산된 숫자 와 계산할때 사용된 숫자의 갯수 변수에 담기
        current_sum, i = answer_deque.popleft()
        
        # 만약 현재까지 사용된 숫자가 numbers와 같다면 조건 통과
        if i == len(numbers):
            # 위에 조건에서 통과된 수중 taget과 같다면 조건 통과
            if current_sum == target:
                # 조건에 모두 부합하다면 answer +1
                answer += 1
        else:
            # 조건 1에서 부합하지 않으면 더하거나 빼는 경우의수를 answer_deque에 담기
            answer_deque.append((current_sum + numbers[i], i + 1))
            answer_deque.append((current_sum - numbers[i], i + 1))
    
    return answer
