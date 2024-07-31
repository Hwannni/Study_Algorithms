def solution(d,budget):
    # d정렬 후 for문 돌면서 budget에서 빼기
    count = 0
    d_sort = sorted(d)
    for i in d_sort :
        if i <= budget :
            count += 1
            budget -= i
    return count
        
        