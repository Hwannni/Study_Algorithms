def solution(n, lost, reserve):
    # set을 만들기
    # reserve와 lost에 공통으로 존재하는 학생을 제거해야 한다.
    reserve_only = list(set(reserve) - set(lost))
    lost_only = list(set(lost) - set(reserve))
    
    # reserve_olny를 기준으로 앞뒤를 확인하여 체육복을 빌려준다.
    for i in reserve_only:
        # 앞의 학생은 -1
        lost_front = i - 1
        # 뒤의 학생은 +1
        lost_back = i + 1
        # 만약 잃어버린 학생의 집합(lost_only)에 front가 있다면 
        if lost_front in lost_only:
            # lost_only에서 front 학생을 제거한다.-> 즉, 빌려주기에 성공했다.
            lost_only.remove(lost_front)
        # 만약 잃어버린 학생의 집합(lost_only)에 back이 있다면
        elif lost_back in lost_only:
            # lost_only에서 back 학생을 제거한다.-> 즉, 빌려주기에 성공했따. 
            lost_only.remove(lost_back)

    # 최대한 나눠준 뒤에 lost_only에 남아있는 학생들은 체육복이 없는 학생들이다.
    return n - len(lost_only)
    
    