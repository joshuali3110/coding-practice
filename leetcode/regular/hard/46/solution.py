# https://leetcode.com/problems/permutations/description/

# optimal solution uses swapping on the original list, then makes copies to add to res

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(curr):
            if curr == n:
                res.append(nums.copy())
            
            for i in range(curr, n):
                nums[curr], nums[i] = nums[i], nums[curr]
                backtrack(curr + 1)
                nums[curr], nums[i] = nums[i], nums[curr]
        
        backtrack(0)
        return res