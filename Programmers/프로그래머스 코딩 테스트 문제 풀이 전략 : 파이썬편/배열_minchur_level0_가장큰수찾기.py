def solution(array):
    # 가장 큰수 찾기
    big_num = max(array)
    # 가장 큰수로 인덱스번호 찾아서 answer에 담아주기
    answer = [big_num,array.index(big_num)]
    return answer