def solution(progresses, speeds):
    answer = []
    
    # progresses와 speeds를 이용해서 각 작업이 100%에 도달하는 데 걸리는 일수를 구하자.
    days = []
    for i in range(len(progresses)):
        # work는 잔여진도를 담은 변수
        work = 100 - progresses[i]
        # 잔여일수와 speeds를 나눠 정수만 plus_day에 담기
        plus_day = work // speeds
        # 잔여 진도와 speed를 나눠 나머지가 0이 아니면 days_needed 1증감 
        if work % speeds != 0:
            plus_day += 1
        days.append(plus_day)
    return days
            
    # 앞에서부터 작업을 확인하면서, 배포 가능한지 판단
    