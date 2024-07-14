def solution(nums):
    # 폰켓몬의 종류 수 
    unique_num = len(set(nums))

    # 골라야 하는 폰켓몬의 수가 폰켓몬의 종류보다 많다면!
    if len(nums) // 2 > unique_num:
        # 폰켓몬 종류의 수를 리턴
        return unique_num
    
    else:
        # 그외에는 골라야 하는 폰켓몬의 수를 리턴
        return len(nums) // 2