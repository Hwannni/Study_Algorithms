def solution(ingredient):
    answer = 0
    
    # 햄버거 스택 초기화
    hamburger = []
    
    # ingredient 요소 순회
    for i in ingredient:
        # 햄버거에 쌓아주기
        hamburger.append(i)
        
        # 햄버거의 생성 조건
        # 1,2,3,1
        # 즉, 숫자 4개의 나열 == 1,2,3,1 이어야 한다.
        # 스택구조에서 숫자의 나열은 슬라이싱으로 표현 가능
        if hamburger[-4:]==[1,2,3,1]:
            # 햄버거 추가!
            answer+=1
            # 만들었으면 해당 요소들은 pop!
            for k in range(4):
                hamburger.pop()
            
    return answer