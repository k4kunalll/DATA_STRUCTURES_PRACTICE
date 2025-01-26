from typing import List

def maxSubArray(nums: List[int]) -> int:
    current_sum, max_sum = nums[0],nums[0]
    for i in nums[1:]:
        if current_sum + i > i:
            current_sum = current_sum + i
        else:
            current_sum = i
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    output = maxSubArray(nums)
    print(maxSubArray(nums))