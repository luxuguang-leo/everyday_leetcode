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
            return True #表示有环
        if l_visit[node] == 1:
            return False
        l_visit[node] = 0
        for neigh in graph[node]:
            if(self.dfs(neigh, graph, l_visit)):
                return True #DFS过程中发现邻居有环，也需要马上判断
        l_visit[node] = 1
        return False

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #DFS,使用深搜标记有无访问过来遍历整个DAG
        '''
        graph = collections.defaultdict(list)
        l_visit = [-1]*numCourses
        for v, k in prerequisites:
            graph[k].append(v)
        for node in xrange(numCourses):
            if(self.dfs(node, graph, l_visit)):
                return False
        return True
        '''
        #BFS,利用优先队列，根据入度是否为零来判断，如果入度为0，则入队列
        #出队列后更新整个inDegree结果，继续在结果中找到入度为0的元素
        #知道整个队列为空，如果有环，则最终结束的时候inDegree数组并不为空
        #我遇到的难点是如何在队列中inDegree为0的值更新整个map
        #@0304,标准topological sort，判断有向图有无环
        '''
        graph = collections.defaultdict(list)
        dq = collections.deque()
        inDegree = [0]*numCourses
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            inDegree[pair[0]] +=1
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                dq.append(i)
        cnt = 0
        while dq:
            node = dq.popleft()
            cnt +=1
            for neigh in graph[node]:
                inDegree[neigh] -=1
                if inDegree[neigh]==0:
                    dq.append(neigh)
        return cnt == numCourses
        '''
        #@DFS
        if not prerequisites:
            return True
        graph = collections.defaultdict(list)
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
        visited = [-1]*numCourses
        for node in range(numCourses):
            if self.dfs(node, graph, visited):
                return False
        return True



        
# @lc code=end

