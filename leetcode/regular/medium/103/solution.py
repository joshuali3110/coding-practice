# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []

        def inOrder(curr, level):
            if curr is None:
                return

            if level >= len(levels):
                levels.append([])
            
            levels[level].append(curr.val)
            
            inOrder(curr.left, level + 1)
            inOrder(curr.right, level + 1)

        inOrder(root, 0)

        for i in range(1, len(levels), 2):
            levels[i].reverse()
        
        return levels