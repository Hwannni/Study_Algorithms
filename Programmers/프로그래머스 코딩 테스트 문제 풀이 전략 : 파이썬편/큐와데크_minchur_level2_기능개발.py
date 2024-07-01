def solution(progresses, speeds):
    # 정답을 담을 리스트 생성하기
    answer = []
    # 여러번 반복해야 하므로 while문 돌리기
    while True :
        # while문 break하는 조건문 생성하기
        if len(progresses) == 0:
            break
        
        # 진행률에 속도더하는 for문 생성하기
        for work in range(len(progresses)):
            progresses[work] += speeds[work]
            # 만약, 100이상이면 100으로 맞추기
            if progresses[work] >= 100:
                progresses[work] = 100
        # count변수 생성하기
        count = 0
        # 100이 앞에서부터 몇개인지 카운트하고 센건 삭제하기
        while progresses and progresses[0] == 100: 
            count += 1
            del progresses[0]
            del speeds[0]  
        # 만약 count가 0 초과이면 answer에 추가하기
        if count > 0:  
            answer.append(count)


    return answer