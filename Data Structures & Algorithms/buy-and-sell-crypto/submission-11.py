class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        b = 0
        for s in range(len(prices)):
            if prices[s] < prices[b]:
                b = s
                continue
            curProf = prices[s] - prices[b]
            prof = max(prof, curProf)
        return prof

        