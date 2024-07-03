def solution(my_string):
    answer = ''
    
    # 먼저 리스트로 변환 -> 각 원소의 중복 제거와 for문 사용을 위해
    list_string = list(my_string)
    
    for i in my_string:
        # 중복 제거를 위해 not in 사용
        if i not in answer:
            # answer에 i의 값이 없다면 추가해라!
            answer += i
            
    return answer