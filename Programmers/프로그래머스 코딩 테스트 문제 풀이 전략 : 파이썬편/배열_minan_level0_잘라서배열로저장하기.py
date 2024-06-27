def solution(my_str, n):
    answer = []
    # while 문 사용을 위한 변수 초기화
    num = 0
    
    # while문 사용 (범위는 0부터 리스트 my_str의 길이까지)
    while num < len(my_str):

        # answer에 append -> 슬라이싱 이용
        answer.append(my_str[num:num+n])

        # 다음 반복을 위한 증감 연산자
        num += n
        
    return answer