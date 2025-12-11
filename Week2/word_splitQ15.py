def word_frequency_counter():
    
    # Get input 
    sentence = input("Enter a sentence: ")
    
    # Split sentence 
    words = sentence.split()
    
  
    frequency = {}
    
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1   
    
    
    print(frequency)


word_frequency_counter()