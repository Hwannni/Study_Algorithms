# 항상 ICN에서 출발
# [a,b] a에서 b로 가는 항공권
# 모든 항공권 소모해야함
# 가능한 경로 2개 이상일 경우 알파벳 순서로 경로 return
# 방문 못하는 경우는 없음
# 1. tickets을 딕셔너리화 하기
# 2. value값들을 정렬하기
# 3. dfs함수로 무한 루프 돌리기
def dfs(cur,ticket_dic,trip,total):
    if len(trip) == total:
        return trip
    else :
        cur = ticket_dic[cur].pop(0)
        trip.append(cur)
        return dfs(cur,ticket_dic,trip,total)

def solution(tickets):
    # 빈 딕셔너리 생성하기
    ticket_dic = {}
    # 현재위치를 담아둘 변수생성하기
    cur = "ICN"
    # 정답에 쓸 빈 리스트 생성하기
    trip = ["ICN"]
    # 총 들릴수 있는 곳 파악하기
    total = len(tickets) + 1
    for ticket in tickets:
        # ticket_dic안에 없으면 생성하기
        if ticket[0] not in ticket_dic:
            ticket_dic[ticket[0]] = [ticket[1]]
        # ticket_dic안에 있으면 추가하기
        else :
            ticket_dic[ticket[0]].append(ticket[1])
            # 정렬해주기
            ticket_dic[ticket[0]] = sorted(ticket_dic[ticket[0]])
            

    answer = dfs(cur,ticket_dic,trip,total)
    return answer
        
    
    