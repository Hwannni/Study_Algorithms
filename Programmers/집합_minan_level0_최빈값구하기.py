def solution(array):
    num = 0
    answer = 0

    # set(array) 요소를 순회
    for i in set(array):
        # array의 요소를 count하며 num보다 크다면 answer을 갱신
        if array.count(i) > num:
            num = array.count(i)
            answer = i
        # 만약 array의 i 의 count가 num과 같다면 최빈값이 동일한 값이 있다는 뜻이로 -1 을 return
        elif array.count(i) == num:
            answer = -1
    return answer