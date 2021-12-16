class Solution:
    def twoSum(self, nums, target): # 2 7 11 15
        dic = {}
        for idx, ele in enumerate(nums):
            diff = target - ele
            if diff in dic:
                return [dic[diff], idx]
            else:
                dic[ele] = idx # record