# https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/description/

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        prev = [1, 1]
        longest = 1

        for i in range(1, len(nums1)):
            nxt = [-1, -1]

            if nums1[i] >= nums1[i - 1]:
                nxt[0] = prev[0] + 1
            if nums1[i] >= nums2[i - 1]:
                nxt[0] = max(nxt[0], prev[1] + 1)
            if nxt[0] == -1:
                nxt[0] = 1
            
            if nums2[i] >= nums1[i - 1]:
                nxt[1] = prev[0] + 1
            if nums2[i] >= nums2[i - 1]:
                nxt[1] = max(nxt[1], prev[1] + 1)
            if nxt[1] == -1:
                nxt[1] = 1
            
            longest = max(max(nxt), longest)
            prev = nxt

        return longest
                