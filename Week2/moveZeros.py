def moveZeroes(nums):
    print(f"Original array: {nums}")
    print("-" * 40)
    
    
    count_non_zero = 0
    
   
    for i in range(len(nums)):
        print(f"Checking position {i}: value = {nums[i]}")
        
        if nums[i] != 0:
            print(f"  Found non-zero: {nums[i]}")
            print(f"  Moving {nums[i]} from position {i} to position {count_non_zero}")
            
            
            nums[count_non_zero] = nums[i]
            count_non_zero += 1
            
            print(f"  Array after move: {nums}")
        else:
            print(f"  Found zero, skipping...")
        print()
    
    print("-" * 40)
    print(f"After moving non-zeros: {nums}")
    print(f"Next zero should go at position: {count_non_zero}")
    print("-" * 40)
    
    
    for i in range(count_non_zero, len(nums)):
        print(f"Setting position {i} to 0")
        nums[i] = 0
    
    print("-" * 40)
    print(f"Final array: {nums}")
    
    return nums


nums = [0,1,0,3,12]
moveZeroes(nums)