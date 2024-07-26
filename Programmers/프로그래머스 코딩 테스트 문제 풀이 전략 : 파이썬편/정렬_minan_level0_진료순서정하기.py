def solution(emergency):
    answer = []
    sort_numbers = sorted(emergency, reverse=True)
    
    for i in emergency:
        answer.append(sort_numbers.index(i)+1)


    return answer