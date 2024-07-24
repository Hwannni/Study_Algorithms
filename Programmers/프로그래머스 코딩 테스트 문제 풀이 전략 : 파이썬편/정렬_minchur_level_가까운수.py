def solution(array,n):
    # array 정렬한번 하기
    array = sorted(array)
    # 차이의 절댓값을 담아둘 리스트 만들기
    abs_lst = []
    # for문 돌리기
    for arr in array:
        abs_ = abs(n-arr)
        abs_lst.append(abs_)
    min_num = min(abs_lst)
    min_ind = abs_lst.index(min_num)
    return array[min_ind]