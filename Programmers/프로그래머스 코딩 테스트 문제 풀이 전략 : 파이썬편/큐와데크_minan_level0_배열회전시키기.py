# 데크 사용을 위한 import
from collections import deque

def solution(numbers, direction):
    # 주어진 numbers를 데크 구조로 변환
    d_number = deque(numbers)
    
    # 만약 right라면 데크에서 가장 오른쪽 원소를 pop
    if direction == "right":
        temp = d_number.pop()
        # pop으로 추출한 원소를 다시 appendleft를 이용하여 맨 왼쪽에 추가
        d_number.appendleft(temp)
        
    # 만약 left라면 데크에서 가장 왼쪽 원소를 popleft
    elif direction == "left":
        temp = d_number.popleft()
        # popleft로 추출한 원소를 다시 append를 이용하여 맨 오른쪽에 추가
        d_number.append(temp)
        
    return list(d_number)