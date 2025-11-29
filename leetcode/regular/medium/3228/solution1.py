# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/description/?envType=daily-question&envId=2025-11-13

class Solution:
    def maxOperations(self, s: str) -> int:
        groups = []
        curr_len = 0

        for c in s:
            if c == "1":
                curr_len += 1
            elif curr_len > 0:
                groups.append(curr_len)
                curr_len = 0
        if curr_len > 0:
            groups.append(curr_len)

        sub = 0
        if s[-1] == "1":
            sub = 1
        
        moves = 0
        k = len(groups)
        for i in range(k):
            if i == k - 1 and s[-1] == "1":
                break
            moves += groups[i] * (k - i - sub)
        
        return moves
