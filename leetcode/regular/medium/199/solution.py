# https://leetcode.com/problems/binary-tree-right-side-view/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.levelOrder(root)
        res = []

        for level in self.levels:
            res.append(level[-1])
        
        return res

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.levels = []
        self.helper(root, 0)
        return self.levels

    def helper(self, root, level):
        if root is None:
            return
        
        if level >= len(self.levels):
            self.levels.append([])

        self.levels[level].append(root.val)

        self.helper(root.left, level + 1)
        self.helper(root.right, level + 1)