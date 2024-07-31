def solution(N,stages):
    # 각 스테이지 위치 갯수
    count_lst = []
    for i in range(1,N+2):
        stage = stages.count(i)
        count_lst.append(stage)
    # 실패율 구하기
    fail_lst = []
    for k in range(N):
        if count_lst[k] != 0:
            fail = count_lst[k] / sum(count_lst[k:])
        else :
            fail = 0
        fail_lst.append([k+1,fail])
    
    # 스테이지 출력하기
    fail_lst = sorted(fail_lst,key=lambda x : x[1],reverse=True)
    answer = []
    for m,n in fail_lst :
        answer.append(m)
    return answer