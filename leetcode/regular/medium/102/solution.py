# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        self.helper(root, 0)
        return self.res

    def helper(self, root, level):
        if root is None:
            return
        
        if level >= len(self.res):
            self.res.append([])

        self.res[level].append(root.val)

        self.helper(root.left, level + 1)
        self.helper(root.right, level + 1)