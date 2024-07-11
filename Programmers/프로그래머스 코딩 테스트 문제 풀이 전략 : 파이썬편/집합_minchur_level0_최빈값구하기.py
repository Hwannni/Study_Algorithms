def solution(array):
    # 갯수 셀때 쓸 빈 딕셔너리 만들기
    count_dic = {}
    # array로 for문 돌리기
    for i in array:
        # 조건 1. i가 count_dic에 들어있지 않으면 추가하기
        if i not in count_dic:
            count_dic[i] = 1
        else : 
            count_dic[i] += 1
    # 중간의 쓸 0인 변수 만들기
    a_int = 0
    for key,value in count_dic.items():
        # 만약 a_int 보다 value값이 크면 최신화하기
        if value > a_int :
            answer = key
            a_int = value
        # 만약 a_int와 같은값이 존재한다면 anwer = -1
        elif value == a_int:
            answer = -1
    return answer
            