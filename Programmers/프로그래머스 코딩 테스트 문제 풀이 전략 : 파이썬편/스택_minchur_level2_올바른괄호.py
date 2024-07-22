def solution(s):
    # false일때 조건
    # 조건 1. 양쪽끝이 )(면 false
    if s[0] == ")" or s[-1] == "(":
        return False
    
    # 조건 2. 갯수가 일정하지 않으면 false
    if s.count(")") != s.count("("):
        return False
    
    # 조건 3. 인덱스 n번째 까지 "("가 더 적으면 false
    # for n in range(len(s)):
    #     check = s[:n]
    #     if check.count(")") > check.count("("):
    #         return False
    
    check_r = 0
    check_l = 0
    for n in s:
        if n == "(":
            check_r += 1
        elif n == ")":
            check_l += 1
        if check_l > check_r :
            return False
    return True
    
    