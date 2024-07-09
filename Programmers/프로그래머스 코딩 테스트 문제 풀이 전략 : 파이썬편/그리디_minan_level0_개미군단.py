def solution(hp):
    # 장군개미 수 구하기
    general = hp // 5
    
    # 병정개미 수 구하기
    # 장군개미에 의한 잔여 hp에 나누기 3
    soldier = (hp-(5*general))//3
    
    # 일개미 수 구하기
    # 장군개미와 병정개미에 의한 잔여 hp에 나누기 1
    ants = (hp-(5*general)-(3*soldier))//1
    
    answer = general + soldier + ants
    return answer