# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, float('-inf'))
    
    def helper(self, root, max_in_path):
        if root is None:
            return 0

        new_max = max(root.val, max_in_path)

        return (1 if root.val >= max_in_path else 0) + self.helper(root.left, new_max) + self.helper(root.right, new_max)