# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.k = k

        return self.helper(root)
    
    def helper(self, root):
        if root is None:
            return None
        
        found = self.helper(root.left)

        if found is not None:
            return found

        self.count += 1

        if self.count == self.k:
            return root.val
            
        return self.helper(root.right)

