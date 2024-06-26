def solution(line):
    # 교점을 담기 위한 리스트
    cross_point = []
    
    # 각 변수에 x, y, 정수값 담아주기
    for i in range(len(line)):
        for j in range(len(line)+1):
            A, B, E = line(i)
            C, D, F = line(j)
            
            # 분모 정의
            den = A*D - B*C
            
            # 분자 정의
            if den != 0:
                x_num = B*F - E*D
                y_num = E*C - A*F
                
                x = x_num / den
                y = y_num / den
                
                # 정수 확인
                if x == int(x) and y == int(y):
                    # 정수라면 교점 변수에 append
                    cross_point.append((int(x), int(y)))
                
                
            
    answer = []
    return answer