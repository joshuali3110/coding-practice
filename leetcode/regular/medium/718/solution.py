# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/

# dp[i][j] is the length of the longest common postfix of nums1[:j] and nums2[:i] (happened to flip i and j in my code); this is more intuitive to me then using longest prefix, as then you have to conceptually build the dp array from the bottom right instead of top left

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        prev = []
        res = 0

        for num in nums1:
            if num == nums2[0]:
                prev.append(1)
                res = 1
            else:
                prev.append(0)

        for i in range(1, n):
            nxt = [1 if nums2[i] == nums1[0] else 0]

            for j in range(1, m):
                if nums2[i] == nums1[j]:
                    nxt.append(prev[j - 1] + 1)
                else:
                    nxt.append(0)
            
            res = max(max(nxt), res)
            prev = nxt
        
        return res