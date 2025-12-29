# https://leetcode.com/problems/delete-and-earn/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = Counter(nums)
        mn, mx = min(nums), max(nums)
        prev = [counts[mn] * mn, 0]

        for n in range(mn + 1, mx + 1):
            prev = [prev[1] + counts[n] * n, max(prev)]
        
        return max(prev)