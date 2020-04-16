#
# @lc app=leetcode id=332 lang=python
#
# [332] Reconstruct Itinerary
#

# @lc code=start
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        #DFS+递归
        #1.大概思想，使用邻接表，但是要对邻接表排序
        #2.从"JFK"开始DFS，如果遇到终点且不是最终终点，证明这个点是最终要访问的，加入res中
        #3.然后从刚才路径开始回溯
        #4.重复2，3知道栈为空，访问了所有的结点
        #反转res,就是所需要的路径
        if not tickets:
            return []
        graph = collections.defaultdict(list)
        for pair in tickets:
            graph[pair[0]].append(pair[1])
        for src in graph.keys():
            graph[src].sort(reverse = True)
        stack = []
        res = []
        stack.append("JFK")
        while stack:
            elem = stack[-1]
            if elem in graph and len(graph[elem]) > 0:
                stack.append(graph[elem].pop())
            else:
                res.append(stack.pop())
        return res[::-1]
        
# @lc code=end

