def solution(num):
    # 반복 횟수를 담을 변수 정의
    result = 0
    
    # 만약 num이 1이면 0 리턴
    if num == 1:
        return 0
    
    # while문 사용하여 1이 될 때까지 반복
    while num != 1:
        # 먼저 반복 횟수가 500번 이상일시 -1을 리턴
        if result >= 500:
            return -1
        # 짝수인지 판별
        if num % 2 == 0:
            # 짝수일 경우 2로 나누기
            num = num // 2
        # 홀수인지 판별 (코드 상으로는 "짝수가 아니라면" 이라는 뜻으로 else문 사용)
        else:
            # 홀수일 경우 x3 +1
            num = num * 3 + 1
        # 반복횟수에 1 증감
        result += 1
        
    return result