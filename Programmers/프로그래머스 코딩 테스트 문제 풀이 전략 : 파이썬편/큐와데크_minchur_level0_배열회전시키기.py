def solution(numbers,direction):
    # "right"인지 "left"확인하기
    if direction == "right":
        return [numbers[-1]] + numbers[:-1]
    else :
        return numbers[1:] + [numbers[0]]