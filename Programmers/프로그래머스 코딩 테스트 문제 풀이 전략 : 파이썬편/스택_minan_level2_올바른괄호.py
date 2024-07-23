def solution(s):
    # 스택 초기화
    stack = []
    
    # 주어진 문자열을 순회
    for i in s:
        # 스택에 요소 push
        stack.append(i)
        # 만약 마지막 요소 2개가 "()" 을 경우 안쪽 for문 시행
        if stack[-2:] == ["(", ")"]:
            # 두 번 반복
            for k in range(2):
                # 주어진 횟수만큼 pop
                stack.pop()
        
    # 만약 스택에 요소가 없으면 Ture, 아니라면 False 라는 조건을 is_empty 변수에 저장 
    is_empty = True if len(stack) == 0 else False
    
    # 결과 리턴
    return is_empty
        