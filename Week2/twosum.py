def twoSum(nums, target):
    
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[num] = i
    
    return []

def test_twoSum():
    """Test the function with various test cases"""
    test_cases = [
        # (nums, target, expected_output)
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
    ]
    
    print("Testing Two Sum Problem")
    print("=" * 50)
    
    for i, (nums, target, expected) in enumerate(test_cases):
        print(f"\nTest Case {i+1}:")
        print(f"  Input: nums = {nums}, target = {target}")
        
        result = twoSum(nums, target)
        print(f"  Output: {result}")
        print(f"  Expected: {expected}")
        
        
        if sorted(result) == sorted(expected):
            print("PASS")
        else:
            print("FAIL")
    
    print("\n" + "=" * 50)


test_twoSum()