# https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_path = 0

        self.depth(root)
        return self.max_path

    def depth(self, root):
        if root is None:
            return -1
        
        depth_left = 1 + self.depth(root.left)
        depth_right = 1 + self.depth(root.right)

        self.max_path = max(self.max_path, depth_left + depth_right)

        return max(depth_left, depth_right)
        
        