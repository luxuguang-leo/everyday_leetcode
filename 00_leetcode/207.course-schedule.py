#
# @lc app=leetcode id=207 lang=python
#
# [207] Course Schedule
#

# @lc code=start
class Solution(object):
    def dfs(self, node, graph, l_visit):
        #-1, init state
        #1, visited,return immediately
        #0,visiting, has circule
        if l_visit[node] == 0:
            return True
        if l_visit[node] == 1:
            return False
        l_visit[node] = 0
        for neigh in graph[node]:
            if(self.dfs(neigh, graph, l_visit)):
                return True
        l_visit[node] = 1
        return False

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(list)
        l_visit = [-1]*numCourses
        for v, k in prerequisites:
            graph[k].append(v)
        for node in xrange(numCourses):
            if(self.dfs(node, graph, l_visit)):
                return False
        return True
        
# @lc code=end

