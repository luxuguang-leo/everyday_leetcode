#
# @lc app=leetcode id=257 lang=python
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, path,  ret):
        if not root.left and not root.right:
            ret.append(path)
            return
        if root.left:
            self.dfs(root.left, path+"->"+str(root.left.val), ret)
        if root.right:
            self.dfs(root.right, path+"->"+str(root.right.val), ret)
        return ret
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        #DFS,递归终止点是为空节点，叶子节点
        '''
        if not root:
            return []
        ret = []
        self.dfs(root, str(root.val), ret)
        return ret
        '''
        #DFS, with stack
        '''
        if not root:
            return []
        stack = [(root, str(root.val))]
        ret = []
        while stack:
            node, path = stack.pop()
            #don't care the right or left first, because only path is needed
            if node.right:
                stack.append((node.right,path+"->"+str(node.right.val)))
            if node.left:
                stack.append((node.left, path + "->"+str(node.left.val)))
            if not node.left and not node.right:
                ret.append(path)
        return ret
        '''
        #BFS, with queue,比较巧妙，刚开始没有看懂，for循环的话一直往队列中增加元素，在上一次的path基础上添加节点，
        #最后一个叶子节点，打印出整个路径，注意并不需要出队列，因为只需要打印所有路径
        #此方法和上一个方法共同点在于：
        #路径是由parent和当前节点构成，用path记录，每一次的path都会更新
        if not root:
            return []
        q, ret = [(root, str(root.val))] ,[]
        for node, path in q:
            if node.left:
                q.append((node.left, path+"->"+str(node.left.val)))
            if node.right:
                q.append((node.right, path+"->"+str(node.right.val)))
            if not node.left and not node.right:
                ret.append(path)
        #print(q)
        return ret

                        



        
# @lc code=end

