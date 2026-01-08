# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/

# my initial solution, cool approach with binary search, but entirely unnecessary for this problem; beats 5%

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.k = k
        left = k - 1
        right = len(nums) + 1

        while right > left + 1:
            mid = (right + left) // 2
            if self.scan(mid):
                left = mid
            else:
                right = mid
        
        return left
    
    def scan(self, length):
        counts = defaultdict(int)
        over = 0
        for i in range(len(self.nums)):
            if i >= length:
                counts[self.nums[i - length]] -= 1
                if counts[self.nums[i - length]] == self.k:
                    over -= 1

            counts[self.nums[i]] += 1
            if counts[self.nums[i]] == self.k + 1:
                over += 1

            if i >= length - 1 and over == 0:
                return True
        return False