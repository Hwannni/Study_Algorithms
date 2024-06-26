def solution(rows, columns, queries):
    
    # 행렬 초기화
    matrix = []

    # 먼저 빈 행렬 만들기
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(0)
        matrix.append(row)
    
    # 1부터 숫자 시작하니까 num 미리 정의
    num = 1
    
    # 빈 행렬에 row, cloumns 수에 따라 값 채우기
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = num
            # num 증감
            num += 1
    
    answer = []
    return answer