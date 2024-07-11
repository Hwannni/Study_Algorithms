def solution(array):
    result = 0
    
    for num in array:
        str_num = str(num)
        print(str_num)
        
        # 변환된 문자열에서 '7'의 개수를 셈
        result += str_num.count('7')

    return result