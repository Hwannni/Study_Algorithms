def solution(n, lost, reserve):
    answer = 0
    
    # 차집합으로 중복되지 않는 lost,reserve 구하기
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    # set_reserve로 for문 돌리면서 i-1,i+1이 있는지 찾아보기
    for i in set_reserve :
        if i-1 in set_lost :
            set_lost.remove(i-1)
        elif i+1 in set_lost :
            set_lost.remove(i+1)
    answer = n - len(set_lost)
    return answer