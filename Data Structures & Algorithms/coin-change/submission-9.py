class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for amt in range(1, amount + 1):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(1 + dp[amt - coin], dp[amt])
        if dp[-1] != amount + 1:
            return dp[-1]
        else:
            return -1

        