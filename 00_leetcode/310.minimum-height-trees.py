#
# @lc app=leetcode id=310 lang=python
#
# [310] Minimum Height Trees
#

# @lc code=start
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        #无向图，BFS，大概思路是使用邻接表构建图，然后将度为1的节点BFS，遍历过程中
        #如果度降为1，则继续BFS，每一层度相同的节点保存起来，最后一层的节点应该就是所求的节点
        if n == 1:
            return [0]
        graph = collections.defaultdict(list)
        queue = collections.deque()
        indegree = [0]*n
        for pair in edges:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
            indegree[pair[0]] +=1
            indegree[pair[1]] +=1
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
        while queue:
            path = []
            for _ in range(len(queue)):
                vertex = queue.popleft()
                path.append(vertex)
                for neigh in graph[vertex]:
                    indegree[neigh] -=1
                    if indegree[neigh] == 1:
                        queue.append(neigh)
        return path


        
# @lc code=end

