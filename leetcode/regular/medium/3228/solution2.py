# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/description/?envType=daily-question&envId=2025-11-13

class Solution:
    def maxOperations(self, s: str) -> int:
        groups = 0
        if s[-1] == "0":
            groups = 1
        curr_length = 0
        ops = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                curr_length += 1
            elif curr_length > 0:
                ops += curr_length * (groups)
                groups += 1
                curr_length = 0

        return ops + curr_length * groups
            
