def solution(arr):
    answer = []
    
    # arr의 길이만큼 반복
    for i in range(len(arr)):
        # arr의 원소들을 차례로 answer에 append
        answer.append(arr[i])
        
        # 만약 answer의 원소가 연속된다면 pop!
        # 연속되는지 비교하기 이전에 인덱스 i가 arr의 길이를 벗어나지 않는지 확인!
        # 이를 지키지 않으면 인덱스 범위를 초과했다는 에러 발생
        if i < len(arr) - 1 and answer[-1] == arr[i+1]:
            answer.pop()

    return answer