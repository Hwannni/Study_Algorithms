def solution(num_list,n):
    # 정답에 쓸 리스트 만들기
    answer_lst = []
    # num_list의 전체 길이 구하기
    length = len(num_list)
    # "num_list의 길이는 n의 배 수개입니다."라고 했으므로 //로 나누기만 하자
    for_n = length//n
    for i in range(for_n):
        # index out of range 오류가 날 수 있으므로 맨 마지막은 조건 추가
        if i == for_n-1 :
            answer = num_list[n*i:]
            answer_lst.append(answer)
        else :
            answer = num_list[n*i:n*(i+1)]
            answer_lst.append(answer)
    return answer_lst
    