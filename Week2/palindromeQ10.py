def isPalindrome(x):
    
   
    num_str = str(x)
    
    # Check if string equals its reverse
    return num_str == num_str[::-1]

print(isPalindrome(121))  
print(isPalindrome(-121)) 
print(isPalindrome(10))  
