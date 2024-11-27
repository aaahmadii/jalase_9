def avglengh(*args):
    punc = ["?", ",", "!"]
    total_length = 0
    word_count = 0
    
    for i in args:
        if i not in punc:
            total_length += len(i) 
            word_count += 1  
            
    if word_count == 0:
        return 0
    
    average_length = total_length / word_count  
    return average_length


m = avglengh("salam", "amir", "ali?")  
print(f"میانگین طول کلمات: {m}")
