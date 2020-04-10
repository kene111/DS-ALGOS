"""
def max_subarray(numbers):
    best_sum = 0
    current_sum = 0

    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
        return best_sum
"""
'''  
def max_subarray(numbers):
    best_sum = 0
    best_start = 0
    best_end = 0
    current_sum = 0
    for current_end, x in enumerate(numbers):
        if current_sum <= 0:
            current_start = current_end
            current_sum = x
        else:
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start

            best_end = current_end + 1

    return best_sum, best_start, best_end

'''
''' SAMMAD'S SOLUTION 
def max_subarray(nums):
    best_sum = nums[0]
    current_sum = nums[0]
    for x in nums[1:]:
        if current_sum <= 0:
            current_sum = x
        else:
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum

    return best_sum
'''
# MY SOLUTION
def max_subarray(nums):
    best_sum = 0
    current_sum = 0
    for x in nums:
        if current_sum <= 0:
            current_sum = x
        else:
            current_sum += x

        if current_sum > best_sum:
            best_sum = current_sum

    return best_sum


array1 = [-1]


array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

check = max_subarray(array1)
print(check)

