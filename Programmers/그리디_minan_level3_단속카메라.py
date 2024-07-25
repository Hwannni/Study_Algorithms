def solution(routes):
    answer = 0
    # 도착지점 카메라 기준으로 정렬
    sorted_routes = sorted(routes, key=lambda x: x[1], reverse=False)
    # 카메라 지점 설정
    camera = -30000
    
    # 도로 순회
    for i in sorted_routes:
        if i[0] > camera:
            answer += 1
            # 카메라 지점 업데이트
            camera = i[1]
            
            
    return answer