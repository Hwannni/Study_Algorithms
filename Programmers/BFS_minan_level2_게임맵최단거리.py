from collections import deque

def solution(maps):
    # 상하좌우 리스트 만들기
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    # BFS를 위한 빈 큐 생성
    queue = deque()
    # 큐에 초기 위치 설정
    queue.append((0, 0))
        
    # queue가 빌 때까지 
    while queue:
        x, y = queue.popleft()
            # 상하좌우 칸 확인하기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            ### 맵을 벗어나는 조건과  벽을 만나는 조건의 순서를 지켜줘야함
            # 맵을 벗어나면 continue
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): 
                continue
                
            # 벽을 만나면 continue
            if maps[nx][ny] == 0:
                continue
                
            # 경로 진행하기 -> 갱신하면서 진행한다.
            # 조건을 ==1로 해야만 왔던 곳을 되돌아 가는 일이 발생하지 않습니다.
            if maps[nx][ny] == 1:
                # 한 칸 당 거리는 1
                maps[nx][ny] = maps[x][y] + 1
                # 큐에 새로 갱신
                queue.append((nx, ny))
                
    # 마지막 위치 출력
    answer = maps[-1][-1]
    # 마지막 위치가 1이 아니라면 그대로 값을 출력
    if answer != 1:
        return answer
    # 마지막 위치가 1이라면 도착지의 주변이
    # 모두 벽으로 둘러 쌓여있는 형태이므로 -1
    # 즉, 위 while문을 순회해도 
    else:
        return -1