def solution(array, commands):
    # 정답에 쓸 빈 리스트 생성하기
    answer = []
    # commands로 for문 돌리기
    for command in commands:
        # command의 인덱스0번째부터 1번째까지 슬라이싱한걸 변수k에 담아주기
        k = array[command[0]-1:command[1]]
        # k 정렬하기
        k.sort()
        # command의 인덱스2번째의 숫자가 k의 인덱스숫자로 넘어가 answer에 담아주기
        answer.append(k[command[2]-1])
    return answer