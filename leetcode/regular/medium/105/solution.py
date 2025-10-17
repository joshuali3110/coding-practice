# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pre_or = preorder
        self.in_or = inorder
        self.in_idx = {}
        self.idx = 0
        
        for i in range(len(inorder)):
            self.in_idx[inorder[i]] = i

        return self.build(0, len(preorder))
        
    def build(self, start, end):
        if start == end:
            return None
        
        curr_val = self.pre_or[self.idx]
        root = TreeNode(curr_val)

        root_idx = self.in_idx[curr_val]

        self.idx += 1
        root.left = self.build(start, root_idx)
        root.right = self.build(root_idx + 1, end)

        return root

