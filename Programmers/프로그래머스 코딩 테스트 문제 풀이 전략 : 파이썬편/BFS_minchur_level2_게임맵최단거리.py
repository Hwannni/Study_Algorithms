import heapq

def solution(maps):
    # 동서남북으로 이동하는 리스트 구하기
    move = [[1,0],[-1,0],[0,1],[0,-1]]
    # 첫시작 위치 정하기 및 카운트되는 것
    start = [(0,0,1)]
    visited = set([(0,0)])
    heapq.heapify(start)
    # 경기장 길이
    map_ = len(maps)
    while True:
        # 검증 1. 중간에 start안에 아무것도 없으면 -1리턴
        if len(start) == 0:
            return -1
        # 세로 x, 가로 y, 카운팅 i
        x,y,i = heapq.heappop(start)
        # 최종 . 현재위치가 4,4가되면 카운트 리턴
        if x == 4 and y == 4 :
            return i
        i += 1
        for n,m in move :
            x_move = x + n
            y_move = y + m
        # 검증 2. 현재위치의 숫자가 음수면 탈락
            if map_ > x_move >= 0 and map_ > y_move >= 0 :
        # 검증 3. 현재위치의 Maps상 위치가 0이면 탈락
                if maps[x_move][y_move] == 1 and (x_move,y_move) not in visited: 
                    start.append((x_move,y_move,i))
                    visited.add((x_move,y_move,))