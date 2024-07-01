def solution(s):
    answer = []
    # 먼저 split 함수로 공백 제거
    list_s = s.split() 
    
    # for문으로 각 요소 비교
    for i in list_s:
        # i가 숫자인지 판별
        # - 부호는 문자열로 판별되기에 lstrip을 이용해서 제외하고 숫자인지 판별해야함
        if i.lstrip('-').isdigit():
            # answer 리스트에 append
            answer.append(int(i))
            # i가 만약 문자열 Z라면!
        elif i == "Z":
            # 먼저 answer가 비어있으면 pop 에러가 발생하므로
            # answer가 빈 리스트가 아닌지 검증!(검증단계)
            if answer:
                # pop 함수를 이용해 마지막 요소 제거
                answer.pop()
        else:
            continue
            
    # sum()함수로 answer 리스트 안에 있는 요소 더하기        
    result = sum(answer)
    
    
    return result