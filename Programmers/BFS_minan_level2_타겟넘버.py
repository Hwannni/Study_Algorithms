def solution(numbers, target):
    # DFS 사용
    def dfs(n, n_sum):
        # 종료 조건: n이 배열의 길이와 같다면!
        if n == len(numbers):
            # 만약 sum과 targer 값이 같다면 1, 아니라면 0
            if n_sum == target:
                return 1
            else:
                return 0
        
        # 두 가지 경우 정의
        # 1. 더하는 케이스
        first_case = dfs(n + 1, n_sum + numbers[n])
        # 2. 빼는 케이스
        second_case = dfs(n + 1, n_sum - numbers[n])
        
        return first_case + second_case
    
    # 초기 호출
    return dfs(0, 0)
