#
# @lc app=leetcode id=399 lang=python
#
# [399] Evaluate Division
#

# @lc code=start
class Solution(object):
    #DFS表示x/y?,确实，因为比如x = 'a', y = 'b'，graph[]
    def dfs(self, x, y, graph, visited):
        if x not in graph or y not in graph:
            return -1.0
        if x == y:
            return 1.0
        for n in graph[x]:
            if n in visited:
                continue
            visited.add(x)
            d = self.dfs(n, y, graph, visited)
            if d != -1.0:
                #这里如果返回有值，代表x->n可行，继续迭代n->?，并且更新值,递推公式dfs(x,y) = graph[x][n]*dfs(n,y)
                return d*graph[x][n]
        return -1.0

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        #graph, DFS或者BFS,难点是
        # 1.将value转换为有向图，并且是双向的
        # 2.构造graph，使用临界矩阵，邻接矩阵使用python的default(list)来构造,如graph[['a', 'b']]
        #如果使用list来构造邻接矩阵:则graph为 {’b‘:[['a',0.5],['c', 3.0]] , 'a':[['b',2.0]]},表示一个点为graph[x][2]
        #如果使用dict来构造邻接矩阵：则graph为{'b':{'a':0.5, 'c':3.0}, 'a':{'b':2.0}}，表示一个点为graph[x][y],更加容易易于理解
        '''
        if not queries or not values or not queries:
            return [-1.0]
        graph = collections.defaultdict(dict)
        for (x,y), value in zip(equations, values):
            graph[x][y] = value
            graph[y][x] = 1.0/value
        self.ret = []
        for (x,y) in queries:
            self.ret.append(self.dfs(x, y, graph, set()))
        return self.ret
        '''
        #@0306，参考网上的一个BFS解法
        if not queries or not values or not queries:
            return [-1.0]
        graph = collections.defaultdict(list)
        for i in range(len(equations)):
            s, d= equations[i]
            graph[s].append([d, values[i]])
            if values[i]:
                graph[d].append([s, 1.0/values[i]])
        def bfs(A, B, graph = graph):
            if A not in graph or B not in graph:
                return -1
            queue = collections.deque([(A, 1)])
            #queue.append([A, 1])
            visited = set()
            while queue:
                currA, accu = queue.popleft()
                if currA == B:
                    return accu
                if currA not in visited:
                    visited.add(currA)
                    for neigh in graph[currA]:
                        next_node, k = neigh
                        if next_node not in visited:
                            queue.append((next_node, k*accu))
            return -1
        ret = []
        for query in queries:
            A, B = query
            query_ans = bfs(A, B)
            ret.append(query_ans)
        return ret




    

        
# @lc code=end

