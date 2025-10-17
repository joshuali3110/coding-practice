# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        self.helper(root)
        return self.res

    def helper(self, root) -> (int, int):
        if root is None:
            return 0
        
        left = self.helper(root.left)
        right = self.helper(root.right)

        self.res = max(self.res, root.val + left + right)

        return max(0, root.val + max(left, right))