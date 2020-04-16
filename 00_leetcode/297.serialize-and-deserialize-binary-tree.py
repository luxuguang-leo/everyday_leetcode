#
# @lc app=leetcode id=297 lang=python
#
# [297] Serialize and Deserialize Binary Tree
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
        if not root:
            return ''
        ret = []
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node:
                ret.append("#")
                continue
            else:
                ret.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return ",".join(ret)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        q = collections.deque()
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q.append(root)
        cur_pos = 1
        while q:
            node = q.popleft()
            if nodes[cur_pos] != '#':
                node.left = TreeNode(int(nodes[cur_pos]))
                q.append(node.left)
            cur_pos +=1
            if nodes[cur_pos] != '#':
                node.right = TreeNode(int(nodes[cur_pos]))
                q.append(node.right)
            cur_pos +=1
        return root


            

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

