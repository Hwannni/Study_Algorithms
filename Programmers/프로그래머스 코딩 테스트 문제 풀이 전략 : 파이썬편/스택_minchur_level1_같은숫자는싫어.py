def solution(arr):
    # 정답에 쓸 빈 리스트 생성하기
    answer = []
    # arr을 for문 돌리기
    for a in arr :
        # 조건 1. answer에 아무것도 없다면 그냥 채워넣기
        if len(answer) == 0:
            answer.append(a)
        # 조건 2. answer의 마지막 인덱스 값이랑 a와 같지 않다면 채워넣기
        elif answer[-1] != a:
            answer.append(a)
    return answer