def solution(N, number):
    answer = 0
    # 큰 문제를 여러 개의 작은 문제로 쪼개서 접근하는 문제
    
    # 1   2   3   4     5      6      7       8
    # 55 555 555 5555 55555 555555 5555555 55555555 
    # return 값은 8보다 커야한다.
    # 8보다 크게되면 -1을 return 한다.
    # 숫자 N을 한 번 사용해서 만드는 값...
    # 숫자 N을 두 번 사용해서 만드는 값...
    # 이런식으로 점진적으로 값을 도출해야 할거 같다.
    
    return -1