#
# @lc app=leetcode id=437 lang=python
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, sum):
        #注意DFS和pathSum区别，DFS表示一定选root这个结点组成最终的结果
        if not root:
            return 0
        ans_cnt = 0
        if root.val == sum:
            ans_cnt +=1
        ans_cnt += self.dfs(root.left, sum-root.val)
        ans_cnt += self.dfs(root.right, sum-root.val)
        return ans_cnt

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        #DFS+DFS
        # 1.对于每一个结点有两种选择，选或者不选
        #2.注意题目是从上到下的，不是左右皆选的类似，必须从root到结点
        '''
        if not root:
            return 0
        self.hashmap = {}
        return self.pathSum(root.left, sum) + self.pathSum(root.right, sum) + self.dfs(root, sum)
        '''
        #DFS+hashmap
        #另外一种使用hashmap的做法，先记下来，大概思路就是使用一个hashmap记录当前路径和，然后在hashmap中寻找cursum-sum是否在
        #hashmap中，如果存在，则证明存在从root到当前节点的路径
        '''
        self.ans = 0
        cache = collections.defaultdict(int)
        cache[0] = 1

        def acc_dfs(root, cur_sum):
            if not root:
                return 0
            cur_sum += root.val
            self.ans += cache[cur_sum-sum]
            cache[cur_sum] +=1
            acc_dfs(root.left, cur_sum)
            acc_dfs(root.right, cur_sum)
            cache[cur_sum] -=1
        acc_dfs(root, 0)
        return self.ans
        '''
        #另外一种看网上是BFS+DFS比较新鲜
        if not root:
            return 0
        q = collections.deque([root])
        self.ans = 0
        while q:
            node = q.popleft()
            self.ans += self.dfs(node, sum)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return self.ans

        
# @lc code=end

