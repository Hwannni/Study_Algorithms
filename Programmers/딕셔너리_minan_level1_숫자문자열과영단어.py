def solution(s):
    # 영단어-숫자 딕셔너리 정의
    number_dic = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    for key in number_dic:
        # replace() 사용
        # s 문자열에 key가 존재한다면
        # number_dic[key]의 value 값으로 대체한다!
        s = s.replace(key, number_dic[key])
    
    # 정답은 int형으로!
    answer = int(s)
    
    return answer
