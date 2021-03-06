#
# @lc app=leetcode id=133 lang=python
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def dfs(self, node, hashmap):
        if not node:
            return None
        if node in hashmap:
            return hashmap[node]
        node_copy = Node(node.val, [])
        hashmap[node] = node_copy
        for n in node.neighbors:
            n_copy = self.dfs(n, hashmap)
            if n_copy:
                node_copy.neighbors.append(n_copy)
        return node_copy

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        #dq是优先队列
        #hash_map存的是新旧节点
        '''
        if not node:
            return None
        dq = collections.deque([node])
        hashmap = dict()
        node_copy = Node(node.val, [])
        hashmap[node] = node_copy
        while dq:
            edge = dq.popleft()
            #不需要的，因为加入队列的node节点肯定是创建过的节点，否则怎么入队呢？
            #if edge not in hash_map():
                #new_node = Node(edge.val, [])
                #hash_map[edge] = new_node
            for neig in edge.neighbors:
                if neig not in hashmap:
                    hashmap[neig] = Node(neig.val, [])
                    dq.append(neig)
                hashmap[edge].neighbors.append(hashmap[neig])
        return node_copy
        '''
        #DFS，深搜，然后递归
        '''
        if not node:
            return None
        return self.dfs(node, dict())
        '''
        #@0305
        if not node:
            return None
        hashmap = dict()
        hashmap[node] = Node(node.val, [])
        q = collections.deque([node])
        while q:
            edge = q.popleft()
            for neigh in edge.neighbors:
                #寻找1的邻居，如2，3
                if neigh not in hashmap:
                    #将2’ 映射到原有2节点
                    hashmap[neigh] = Node(neigh.val,[])
                    #继续原有图的BFS
                    q.append(neigh)
                #建立1‘和2’的映射关系
                hashmap[edge].neighbors.append(hashmap[neigh])
        return hashmap[node]


        
# @lc code=end

