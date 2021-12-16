class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = prices[0]
        maxsum = 0
        for i in range(1,len(prices)):
            if prices[i] < curr:
                curr = prices[i]
            else:
                curr_pro = prices[i] - curr
                if curr_pro > maxsum:
                    maxsum = curr_pro

        return maxsum



                
        
                