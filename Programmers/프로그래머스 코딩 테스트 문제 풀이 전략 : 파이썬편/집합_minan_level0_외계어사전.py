def solution(spell, dic):
    # spell을 set으로 변환
    # set 자료구조는 순서에 구애받지 않기 때문에 용이하다!
    set_spell = set(spell)
    
    # for문을 사용하여 dic 리스트 순회
    for i in dic:
        # if문을 사용하여 겹치는 단어 확인
        if set(i) == set_spell:
            return 1
    
    return 2