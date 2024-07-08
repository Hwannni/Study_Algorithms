def solution(array, commands):
    answer = []
    for start, end, k in commands:
        sort_array = array[start-1:end]
        # sort 함수로 간단하게 정렬 완료
        sort_array.sort()
        # k번째 요소 선택 (인덱스는 0부터 시작하므로 k-1)
        answer.append(sort_array[k-1])  
    return answer
