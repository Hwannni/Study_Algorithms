def solution(array):
    result = []
    
    max_number = max(array)
    max_index = array.index(max_number)
    
    result.append(max_number)
    result.append(max_index)
    
    
    return result