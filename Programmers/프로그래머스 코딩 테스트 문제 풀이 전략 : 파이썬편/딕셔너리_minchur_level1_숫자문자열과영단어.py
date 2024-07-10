def solution(s):
    # 영문 숫자를 숫자로 매칭하기위해 딕셔너리 생성
    number = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    # 정답에 쓸 빈 문자열 생성
    answer = ''
    # 중간에 사용할 빈 문자열 생성
    a_str = ''
    # s로 For문 돌리기
    for i in s:
        # 만약 i가 숫자라면 answer에 추가
        if i.isdigit():
            print(f'1 : {i}')
            answer += str(i)
        # 없다면 a_str에 추가
        else :
            print(f'2 : {i}')
            a_str += i
        # 만약 a_str문자가 number안에 있다면 answer에 추가하고 a_str 리셋
        if a_str in number:
            print(f'3 : {i}')
            answer += str(number[a_str])
            a_str = ""
    return int(answer)