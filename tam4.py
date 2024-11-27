def firstUChar(s):
    char_count = {}
    
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index  
    
    return -1  
result = firstUChar("swiss")
print(result)  
