def dfs(n, count):
    # n이 1이 되면 count 리턴하기
    if n == 1:
        return count
    # n이 500 초과가 되면 -1리턴하기
    elif count > 500:
        return -1
    else:
        # count +1
        count += 1
        # n이 짝수일 경우
        if n % 2 == 0:
            n = n // 2
        # n이 홀수일 경우
        else:
            n = 3*n + 1
        # dfs 반복하기
        return dfs(n, count)  

def solution(n):
    # n이 처음부터 1일 경우
    if n == 1:
        return 0
    answer = dfs(n, 0)
    return answer
