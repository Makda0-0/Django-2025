def mySqrt(x):
   
    if x == 0:
        return 0
    
    
    for i in range(1, x + 1):
        
        if i * i > x:
            return i - 1
    
    
    return x

print(mySqrt(4))  
print(mySqrt(9)) 
print(mySqrt(0))  