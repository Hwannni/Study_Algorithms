## 예외 테스트 사항 추가
## [[-20, 0], [-14, -5], [-18, -13], [-5, -3]]
## 그냥 정렬했을때
## [[-20, 0], [-14, -5], [-18, -13], [-5, -3]]
## 나간거 기준으로 정렬했을때 
## [[-18, -13], [-14, -5], [-5, -3], [-20, 0]]
def solution(routes):
    # [[-20, -15], [-14, -5], [-18, -13], [-5, -3]]의 인덱스 1번째 기준으로 정렬하기
    routes.sort(key=lambda x : x[1])
    # sorted(routes)
    # 비교를 하기위해 변수 설정
    camera = routes[0][1]
    answer = 1
    print(routes)
    # 만약 camera보다 출발 지점이 크면 camera 갱신
    for route in routes:
        if camera < route[0]:
            camera = route[1]
            answer += 1
            print(route)
            
    return answer