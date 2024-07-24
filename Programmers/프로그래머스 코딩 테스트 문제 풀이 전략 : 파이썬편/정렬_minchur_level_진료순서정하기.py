def solution(emergency):
    emergen = []
    # emergency원소들을 11씩 더해주기
    for em in emergency:
        em += 11
        emergen.append(em)
    # emergency길이 만큼 for문 돌리기
    for eme in range(1,len(emergency)+1):
        max_eme = max(emergen)
        ind_eme = emergen.index(max_eme)
        emergen[ind_eme] = eme
    return emergen