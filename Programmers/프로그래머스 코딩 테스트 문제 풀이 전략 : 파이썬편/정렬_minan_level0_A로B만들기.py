def solution(before, after):
    # 첫 번째 방법 -> 시간초과(60점)
    # reverse_word = before[::-1]
    # return 1 if reverse_word == after else 0

    # 두 번째 방법 -> 시간초과(65점)
    # for i in range(len(before)):
        # if before[i] != after[-(i+1)]:
            # return 0
    # return 1
    
    # 세 번재 방법
    sort_before = sorted(before)
    sort_after = sorted(after)
    for i in range(len(sort_before)):
        if sort_before[i]!=sort_after[i]:
            return 0
    return 1   