# heap를 사용함
import heapq

def solution(n,works):
    # 제일 많은게 먼저 빠져야 하므로 먼저 works를 모두 음수화
    _work = [-work for work in works]
    # heapify화 하기
    heapq.heapify(_work)
    # while문 사용 조건. n 0보다 작아지면 스탑
    while n > 0 :
        n -= 1
        # 제일 작은녀석 즉, 작업량이 제일 많이 남은 걸 담아주기
        many_work = heapq.heappop(_work)
        # 조건 만약 0이면 break
        if many_work == 0:
            break
        # many_work은 현재 음수로 되어있으니까 더해줘서 0하고 가깝게 해준다.
        many_work += 1
        # 다시 넣어주기
        heapq.heappush(_work,many_work)
    # 야근지수 계산법을 적용해서 리턴하기
    return sum([i**2 for i in _work])
    