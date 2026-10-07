class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        i = 0
        j = 1
        for j in range(1, len(prices)):
            if prices[j] <= prices[i]:
                i = j
                continue
            curProf = prices[j] - prices[i]
            maxProf = max(curProf, maxProf)
        return maxProf
            
            



        