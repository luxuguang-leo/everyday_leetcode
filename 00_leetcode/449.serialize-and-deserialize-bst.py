#
# @lc app=leetcode id=449 lang=python
#
# [449] Serialize and Deserialize BST
#

# @lc code=start
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
        def dfs(root):
            if not root:
                return 
            ret.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        ret = []
        dfs(root)
        return ','.join(ret)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        stack = [root]
        for node_str in nodes[1:]:
            node_val = int(node_str)
            if node_val < stack[-1].val:
                stack[-1].left = TreeNode(node_val)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < node_val:
                    last = stack.pop()
                last.right = TreeNode(node_val)
                stack.append(last.right)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

