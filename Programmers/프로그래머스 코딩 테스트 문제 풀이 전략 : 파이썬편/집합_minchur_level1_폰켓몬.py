def solution(nums):
    # nums의 중복제거
    nums_set = set(nums)
    # nums의 길이 절반
    half_nums = len(nums) // 2
    # 만약 nums_set의 길이가 nums의 길이 절반보다 크면 nums의 길이 절반 리턴
    if len(nums_set) >= half_nums :
        return half_nums
    # nums_set의 길이가 더 짧으면 nums_set의 길이리턴
    else :
        return len(nums_set)
    
    