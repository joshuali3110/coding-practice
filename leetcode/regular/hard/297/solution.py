# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""

        q = deque([root])
        serialized = []

        while q:
            curr = q.popleft()

            if curr is None:
                serialized.append("null")
            else:
                serialized.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)

        return ','.join(serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        
        data = data.split(",")
        
        root = TreeNode(int(data[0]))
        q = deque([root])
        
        for i in range(1, len(data), 2):
            curr = q.popleft()

            if data[i] != "null":
                curr.left = TreeNode(int(data[i]))
                q.append(curr.left)
            if data[i + 1] != "null":
                curr.right = TreeNode(int(data[i + 1]))
                q.append(curr.right)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))