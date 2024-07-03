def solution(my_str,n):
    # 정답에 쓸 리스트 만들기
    answer_lst = []
    # 전체길이
    
    length = len(my_str)
    # 전체길이에서 n으로 나눴을때의 수
    length_n = length//n
    # 만약 나머지가 있다면 +1 추가 
    # 이전코드 : if length <= length/n :
    if int(str(length/n).split(".")[1]) > 0:
        length_n += 1
    # my_str 슬라이싱 하기
    for s in range(length_n):
        # index out range 오류가 날수가 있으므로 마지막일경우만 조건 추가
        if s == length_n-1:
            answer = my_str[n*s:]
            # 마지막에 ""가 추가 될수가 있으니까 추가 검증
            if answer != "":
                answer_lst.append(answer)
        else :
            answer = my_str[n*s:n*(s+1)]
            answer_lst.append(answer)
    return answer_lst