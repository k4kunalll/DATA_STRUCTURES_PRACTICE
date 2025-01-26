from typing import List


def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0

    i = 0  # Pointer for the last unique element
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:  # Found a new unique element
            i += 1
            nums[i] = nums[j]
    
    return i + 1  # Number of unique elements

if __name__ == "__main__":
    nums = [1,2,2,3,4]
    output = removeDuplicates(nums)
    print(removeDuplicates(nums))