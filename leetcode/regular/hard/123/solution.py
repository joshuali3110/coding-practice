# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b1 = float('-inf') # max profit if bought first on or before current day
        s1 = 0 # max profit if sold first on or before current day
        b2 = float('-inf') # max profi if bought second on or before current day
        s2 = 0 # max profit if sold second on or before current day

        for i, p in enumerate(prices):
            if i >= 3:
                s2 = max(s2, b2 + p)
            if i >= 2:
                b2 = max(b2, s1 - p)
            if i >= 1:
                s1 = max(s1, b1 + p)      
            b1 = max(b1, -p)
        
        return max(s1, s2)
      