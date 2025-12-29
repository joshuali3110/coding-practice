# https://leetcode.com/problems/delete-and-earn/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        self.counts = defaultdict(int)
        score = 0

        start = 10**4 + 1
        prev = -1

        for i in range(len(nums)):
            self.counts[nums[i]] += 1
            if nums[i] == prev or nums[i] == prev + 1:
                prev = nums[i]
            else:
                score += self.rangeScore(start, prev)
                
                start = nums[i]
                prev = nums[i]
        
        return score + self.rangeScore(start, prev)
    
    def rangeScore(self, start, end):
        prev = [start * self.counts[start], 0]

        for i in range(start + 1, end + 1):
            nxt = [prev[1] + i * self.counts[i], max(prev)]
            prev = nxt
        
        return max(prev)
            