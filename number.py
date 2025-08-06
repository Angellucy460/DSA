# Given a list containing n distinct numbers from 0 to n, find the missing number.



# Input: [3, 0, 1]

# Output: 2
# NOTE: No number limit


def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Example usage:
nums = [3, 0, 1]
print(find_missing_number(nums))  # Output: 2
