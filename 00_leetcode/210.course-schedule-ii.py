#
# @lc app=leetcode id=210 lang=python
#
# [210] Course Schedule II
#

# @lc code=start
class Solution(object):
    #0->1
    def dfs(self, node, graph, visiting):
        #-1, init value
        #0, visiting
        #1, visited
        #return false, meaning cannot continue DFS, has circule
        #return true, meaning DFS finished, no circule
        #If anyone is wondering why self.res.append(node) 
        # works instead of appending the node to the left 
        # of the array (as per the topological sort algorithm),
        #  it is because the direction of edges in the graph is 
        # reversed. If you replace self.graph[pair[0]].append(pair[1]) 
        # with self.graph[pair[1]].append(pair[0]),
        #  you would have to do self.res.insert(0, node) instead.
        if visiting[node] == 0:
            return False
        if visiting[node] == 1:
            return True
        visiting[node] = 0
        for neigh in graph[node]:
            if not self.dfs(neigh, graph, visiting):
                return False
        visiting[node]= 1
        self.ret.insert(0,node)#here for DFS,we cannot just append, we need to insert in the head of the list
        return True

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
        visiting = [-1]*numCourses
        self.ret = []
        for node in xrange(numCourses):
            if not self.dfs(node, graph, visiting):
                return []
        return self.ret
# @lc code=end

