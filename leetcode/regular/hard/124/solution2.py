# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1000

        def helper(curr):
            if curr is None:
                return 0
                        
            left = helper(curr.left)
            right = helper(curr.right)
            
            ret = max(curr.val + left, curr.val + right, curr.val)
            self.res = max([self.res, ret, curr.val + left + right])

            return ret
        
        helper(root)

        return self.res