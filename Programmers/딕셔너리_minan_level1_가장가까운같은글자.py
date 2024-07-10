def solution(s):

    answer = []
    # 딕셔너리 초기화
    dic = {}
    
    # enumerate() 함수 사용
    # 인덱스와 요소를 한 번에 반환해주는 함수
    for i, char in enumerate(s):
        # 딕셔너리에 같은 요소가 존재한다면
        if char in dic:  
            # 현재 위치와 저장된 위치의 차이를 append
            # 딕셔너리의 키-값 반환을 이용
            answer.append(i - dic[char])  
        # 처음 나온 문자라면
        else:  
            # -1을 결과에 추가
            answer.append(-1)  
            
        # 딕셔너리 갱신
        dic[char] = i  

    return answer
