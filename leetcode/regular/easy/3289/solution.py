# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/?envType=daily-question&envId=2025-10-31

# O(1) space, there are shorter/faster algorithms with O(N) space
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            if i == nums[i]:
                continue
            
            while i != nums[i]:
                temp = nums[nums[i]]
                if temp == nums[i]:
                    if res and res[0] == nums[i]:
                        break
                        
                    res.append(nums[i])
                    
                    if len(res) == 2:
                        return res
                
                nums[nums[i]] = nums[i]
                nums[i] = temp
        
        return res