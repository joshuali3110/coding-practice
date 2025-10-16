# https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root):
            if root is None:
                return 0, True
            
            left_depth, left_bal = helper(root.left)
            if not left_bal:
                return left_depth, False

            right_depth, right_bal = helper(root.right)
            if not right_bal:
                return right_depth, False
            
            return max(left_depth, right_depth) + 1, abs(left_depth - right_depth) <= 1
        
        _, res = helper(root)

        return res