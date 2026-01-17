# https://leetcode.com/problems/minimum-penalty-for-a-shop/description/

# delta is the difference from the baseline penalty of never opening, which is simply the Y count in the string, we only need when this delta is minimum

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        delta = 0
        min_delta = 0
        closing = 0

        for i in range(len(customers)):
            delta += 1 if customers[i] == 'N' else -1

            if delta < min_delta:
                closing = i + 1
                min_delta = delta
        
        return closing
        