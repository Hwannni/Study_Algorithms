def solution(spell,dic):
    # answer 설정하기
    answer = 0
    # dic로 for문 돌리기
    for i in dic :
        # 문자 하나하나로 리스트화 시키기
        dic_lst = list(i)
        # dic_lst 중복 제거하기
        set_dic_lst = list(set(dic_lst))
        # 검증 1. spell의 길이와 set_dic_lst의 길이가 맞지 않으면 answer을 2로 설정
        if len(spell) != len(set_dic_lst):
            answer = 2
        else :
            # 검증 2. 만약 길이가 같다면 정렬한뒤 같은지 확인하기
            if sorted(spell) == sorted(set_dic_lst) :
                # 정렬해서 똑같으면 완전 똑같은 것이므로 바로 1 리턴하기
                return 1
            # 같지않으니까 answer을 2로 설정하기
            else :
                answer = 2
        # 만약 For문을 빠져 나왔다면 같은건 없는거이니까 answer를 리턴하기
    return answer