# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = []
        # [max profit if bought for the ith time on or before current day, max profit if sold for the ith time on or before current day]

        for i, p in enumerate(prices):
            if i < 2*k:
                dp.append(float('-inf') if i % 2 == 0 else 0)

            for j in range(len(dp) - 1, 0, -1):
                if j % 2 == 0:
                    dp[j] = max(dp[j], dp[j-1] - p)
                if j % 2 == 1:
                    dp[j] = max(dp[j], dp[j-1] + p)
            dp[0] = max(dp[0], -p)
                
        return max(max(dp), 0)