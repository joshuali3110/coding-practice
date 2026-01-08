# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/

# optimized linear approach, for each position i, find longest good subarray that ends there
# don't need to count number of elements "over", because at the top of each loop, the state is already "good", so that the char being added is the only candidate for being over frequency k

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        n = len(nums)
        res = 1
        left = 0

        for i in range(n):
            counts[nums[i]] += 1
            
            while counts[nums[i]] > k:
                counts[nums[left]] -= 1
                left += 1
            
            res = max(res, i - left + 1)
        
        return res