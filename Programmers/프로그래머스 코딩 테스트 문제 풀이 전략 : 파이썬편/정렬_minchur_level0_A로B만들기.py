# before과 after이 같으면 1 다르면 0 출력하기
def solution(before,after):
    if sorted(before) == sorted(after) :
        return 1
    else :
        return 0