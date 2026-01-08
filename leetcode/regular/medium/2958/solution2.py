# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/

# my initial linear time approach, where for each position i, find the longest good subarray starting from i; ends up being a lot of extra processing compared to other way around

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        n = len(nums)
        over = 0
        res = 1

        counts[nums[0]] += 1
        end = 1

        for i in range(n):
            while end < n and over == 0:
                res = max(res, end - i)
                
                counts[nums[end]] += 1
                if counts[nums[end]] == k + 1:
                    over += 1
                end += 1
            
            if over == 0:
                res = max(res, end - i)
            
            counts[nums[i]] -= 1
            if counts[nums[i]] == k:
                over -= 1
        
        return res