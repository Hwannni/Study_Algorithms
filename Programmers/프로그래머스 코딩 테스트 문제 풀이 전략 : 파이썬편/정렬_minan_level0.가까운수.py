def solution(array, n):
    answer = 0
    numbers = []
    
    array.sort()
    
    for i in array:
        numbers.append(abs(n-i))
        
    num_index = numbers.index(min(numbers))
    answer = array[num_index]
    
    
    
    return answer