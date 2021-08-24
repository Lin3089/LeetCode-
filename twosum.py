class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            j = target-i
            first_index = nums.index(i)
            second_index = nums.index(i)+1
            check_list = nums[second_index:]
            if j in check_list:
                return(nums.index(i),second_index+check_list.index(j))
        