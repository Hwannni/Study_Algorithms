# 교점에 별 만들기
* [프로그래머스 - 교점에 별 만들기 - Level 2](https://school.programmers.co.kr/tryouts/72046/challenges?language=python3)
### 설계하기
1. 교점구하기
2. 교점에서 정수로만 된 값을 찾기
3. x좌표의 차 y좌표의 차로 "...."로된 리스트를 만들기
4. "*"의 알맞는 위치에 표시하기
```
def solution(line):
    # 정답 리스트
    answer = []
    # 교점만 모아둘 리스트
    cross = []
    # 교점을 찾는다.
    for i in range(len(line)) :
        for k in line[i+1:] :
            lst = line[i]
            # 평행 검증
            if lst[0]*k[1] - lst[1]*k[0] == 0:
                pass
            else :
                # 교점의 x좌표 구하기
                x = (lst[1]*k[2] - lst[2]*k[1]) / (lst[0]*k[1] - lst[1]*k[0])
                # 교점의 y좌표 구하기
                y = (lst[2]*k[0] - lst[0]*k[2]) / (lst[0]*k[1] - lst[1]*k[0])
                # 정수 검증하기 위한 x,y좌표 리스트화하기
                x_lst = str(x).split(".")
                y_lst = str(y).split(".")
                # 교점에서 정수로만 된 값을 찾기
                if int(x_lst[1]) > 0 or int(y_lst[1]) > 0:
                    pass
                else :
                    if [int(x_lst[0]),int(y_lst[0])] in cross :
                        pass
                    else :
                        # 교점이 정수로만 되어있으면 교점만 모아둘 리스트에 담아두기
                        cross.append([int(x_lst[0]),int(y_lst[0])])
    # x,y좌표들의 최대 최솟값을 구하기 위해 따로 분리해서 담기위해
    x_cross = []
    y_cross = []

    for j in cross :
        x_cross.append(j[0])
        y_cross.append(j[1])
    x_point = max(x_cross) - min(x_cross) + 1
    y_point = max(y_cross) - min(y_cross) + 1
    
    # x좌표의 차 y좌표의 차로 "...."로된 리스트를 만든다.
    point_lst = ["."*x_point]*y_point
    if len(point_lst[0]) == 1 :
        if len(cross) > 0 :
            answer.append("*")
    else :
        # 별을 찍는다.
        for l in cross :
            if max(y_cross) == l[1]:
                star_x = 0
                if max(x_cross) == l[0]:
                    star_y = 0
                else :
                    star_y = max(x_cross) - l[0]
            else : 
                star_x = max(y_cross) - l[1]
                if max(x_cross) == l[0]:
                    star_y = 0
                else :
                    star_y = max(x_cross) - l[0]
            if star_x < 0:
                star_x *= -1
            elif star_y < 0:
                star_y *= -1
            lst = list(point_lst[star_x])
            lst[star_y] = "*"
            point_lst[star_x] = "".join(lst)
            
        answer = point_lst
    return answer
```
### 채점 결과
* 정확성: 24.1
* 효율성: 0.0
* 합계: 24.1 / 100.0
### 오답쓰..