class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = -100000
        current = 0
        for num in nums:
            current += num
            if current>max:
                max = current
            if current < 0:
                current = 0
        return max