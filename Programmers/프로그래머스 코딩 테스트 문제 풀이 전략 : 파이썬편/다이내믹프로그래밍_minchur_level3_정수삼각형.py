def solution(triangle):
    # triangle크기에 맞게 0으로된 삼각형 만들기
    zero_tri = [[0]*len(l) for l in triangle]
    # 꼭대기 값은 같게 설정
    zero_tri[0][0] = triangle[0][0]
    
    # 세로로 돌 for문
    for m in range(1,len(triangle)):
        # 가로로 돌 for문
        for n in range(len(triangle[m])):
            # n이 제일 왼쪽꺼 일때
            if n == 0:
                zero_tri[m][n] = zero_tri[m-1][n] + triangle[m][n]
            # n이 제일 오른쪽꺼 일때
            elif n == len(triangle[m]) - 1 :
                zero_tri[m][n] = zero_tri[m-1][n-1] + triangle[m][n]
            # n이 중간에 있는 거 일때
            else :
                # 둘 중에 큰값으로 더하기 어차피 합의 최대를 구하는 것이므로
                zero_tri[m][n] = max(zero_tri[m-1][n-1],zero_tri[m-1][n]) + triangle[m][n]
    return max(zero_tri[-1])