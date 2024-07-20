from collections import deque

def solution(m, n, puddles):
    MOD = 1000000007
    
    # 오른쪽, 아래쪽 이동 방향 리스트
    dx = [0, 1]
    dy = [1, 0]
    
    # BFS를 위한 빈 큐 생성
    queue = deque()
    # 큐에 초기 위치 설정 (0, 0) 추가
    queue.append((0, 0))
    
    # maps 생성
    maps = [] 
    for i in range(m):
        row = [0] * n  # n개의 0을 가진 리스트를 생성하여 한 행을 구성
        maps.append(row)  # 생성된 행을 maps 리스트에 추가
    maps[0][0] = 1  # 시작 지점은 1로 설정
    
    # 웅덩이 위치를 -1로 설정
    for puddle in puddles:
        x, y = puddle
        if 1 <= x <= n and 1 <= y <= m:  
            maps[y - 1][x - 1] = -1
    

    while queue:
        x, y = queue.popleft()
        
        # 오른쪽과 아래쪽 칸 확인하기
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵을 벗어나면 continue
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
                
            # 웅덩이를 만나면 continue
            if maps[ny][nx] == -1:
                continue
                
            # 경로 개수 갱신
            if maps[ny][nx] == 0:
                maps[ny][nx] = maps[y][x] % MOD
                queue.append((nx, ny))
            else:
                maps[ny][nx] = (maps[ny][nx] + maps[y][x]) % MOD
    
    # 마지막 위치의 경로 개수를 출력
    return maps[m - 1][n - 1]