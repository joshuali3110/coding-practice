# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/?envType=daily-question&envId=2025-10-30

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev = 0
        ops = 0

        for height in target:
            if height > prev:
                ops += height - prev
            
            prev = height
        
        return ops