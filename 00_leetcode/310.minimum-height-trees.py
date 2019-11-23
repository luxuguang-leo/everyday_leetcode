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
        #无向图，BFS，邻接向量表，无向图中的邻接向量表为边数,类似topology算法，一层一层遍历所有顶点
        #每一层遍历的度相同的结点，最后一层queue就是到所有结点都最小的那一层结点，加入到最终结果即可
        if n <= 0:
            return []
        if n == 1:
            return [0]
        ret = []
        graph = collections.defaultdict(list)
        deque = collections.deque()
        degree = [0]* n
        for pair in edges:
            graph[pair[0]].append(pair[1])
            graph[pair[1]].append(pair[0])
            degree[pair[0]] +=1
            degree[pair[1]] +=1
        for i, deg, in enumerate(degree):
            if deg == 1:
                deque.append(i)
        #print(deque)
        while deque:
            path = []
            for n in range(len(deque)):
                edge = deque.popleft()
                path.append(edge)
                for adj in graph[edge]:
                    degree[adj] -=1
                    if degree[adj] == 1:
                        deque.append(adj)
            ret = path
        return ret

        
        
        
# @lc code=end

