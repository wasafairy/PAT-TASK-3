def sublist(numbers):
    _sum = 0
    a_sum = set()  # To store _sum
    
    for num in numbers:
        _sum += num
        
        # Check if the _sum is zero
        if _sum == 0 or _sum in a_sum:
            return True
        
        a_sum.add(_sum)
    
    return False

# main code
numbers = [4,2,-3,1,6]
if sublist(numbers):
    print("There is a sublist with a sum of zero.")
else:
    print("There is no sublist with a sum of zero.")
