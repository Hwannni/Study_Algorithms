def solution(array):
    # array안에 있는 숫자들 str로 바꾸기
    str_array = map(str,array)
    # str_array 모든 숫자를 쪼개서 리스트화하기
    str_array_lst = list(str_array)
    # 하나의 문자열로 합치기
    str_all = "".join(str_array_lst)
    # 문자열에서 7의 갯수 카운팅하기
    answer = str_all.count("7")
    return answer