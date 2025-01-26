# Approach 1
def twoSum1(nums, target):
    temp = {}
    for index,i in enumerate(nums):
        diff = target-i
        if diff in temp:
            return [temp[diff], index]
        else:
             temp[i]=index



# Approach 2

def twoSum2(nums, target):
    index_dict = {}
    start=0
    end=len(nums)-1

    for index,i in enumerate(nums):
        index_dict[i]=index
    nums.sort()
    # print(index_dict)
    

    while start<end:
        sum = nums[start]+nums[end]

        if sum < target:
            start=start+1
        elif sum > target:
            end = end-1
        else:
            first_index = index_dict[nums[start]]
            second_index = index_dict[nums[end]]

            if first_index == second_index:
                end -= 1 
            else:
                return [first_index, second_index]
    return [-1,-1]
    


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    # nums = [-1,6,2,-4,3,7,9, 11,5]
    # target = 4
    # twoSum2(nums,target)
    output = twoSum1(nums,target)
    print(output)
    