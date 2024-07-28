# 알파벳을 담고 있는 python 라이브러리
import string
def solution(s, skip, index):
    answer = ""
    
    # string.ascii_lowercase -> 소문자 알파벳을 의미
    alphabet = string.ascii_lowercase
    
    # skip에 포함된 알파벳은 소문자 알파벳 변수에서 제외시킨다
    for i in list(skip):
        alphabet = alphabet.replace(i,"")
        
    # 주어진 s를 순회
    for j in s:
        # 알파벳 리스트에서 j 위치를 find하여 주어진 index 만큼 더해준다.
        # % len()을 한 이유는 알파벳 문자열 길이로 나눈 나머지를 구해줘야 
        # z를 넘어갈 경우 다시 a로 돌아올 수 있다.
        answer += alphabet[(alphabet.find(j) + index) % len(alphabet)]
        
    return answer    