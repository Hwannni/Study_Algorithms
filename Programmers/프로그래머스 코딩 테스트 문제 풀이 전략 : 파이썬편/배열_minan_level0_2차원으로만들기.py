def solution(num_list, n):
    # 1차원 배열로 시작해야 코드 작성하기 쉬움
    answer = []
    
    # for문 사용 -> 0부터 numlist 길이까지, n씩 건너띄면서!
    for i in range(0, len(num_list), n):

        # answer에 append -> 슬라이싱 이용
        answer.append(num_list[i:i+n])
        
    return answer