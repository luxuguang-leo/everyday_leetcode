#
# @lc app=leetcode id=301 lang=python
#
# [301] Remove Invalid Parentheses
#

# @lc code=start
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #1.如果有效加入结果
        #2.如果无效，计算不平衡的左右括弧个数l, r
        #3.尝试DFS，逐渐减小l, r,直到l = r = 0 and s有效括弧平衡，递归结束
        def isValid(s):
            cnt = 0
            for ch in s:
                if ch == '(':
                    cnt +=1
                elif ch == ')':
                    cnt -=1
                if cnt < 0:
                    return False    
            return cnt == 0
        def dfs(s, start, l, r):
            if l ==0 and r ==0 and isValid(s):
                self.ans.append(s)
                return 
            for i in range(start, len(s)):
                if i>= start+1 and s[i] == s[i-1]:
                    continue
                if r > 0 and s[i] == ')':
                    dfs(s[:i] + s[i+1:], i, l, r-1)
                if l > 0 and s[i] == '(':
                    dfs(s[:i] + s[i+1:], i, l-1, r)
        
        def bfs(s, l, r):
            self.visited = set()
            q = collections.deque()
            q.append((s, l, r))
            minFound = False
            while q:
                s, l, r = q.popleft()
                if l == 0 and r == 0 and isValid(s):
                    self.ans.append(s)
                    minFound = True
                if minFound:
                    continue
                for i in range(len(s)):
                    nxt = s[:i]+s[i+1:]
                    if nxt not in self.visited:
                        if s[i] == '(' and l > 0:
                            self.visited.add(nxt)
                            q.append((nxt, l-1, r))
                        if s[i] == ')' and r > 0:
                            self.visited.add(nxt)
                            q.append((nxt, l, r-1))


        #计算不平衡的左右括弧数目
        if not s:
            return [""]
        l, r = 0, 0
        for ch in s:
            if ch == '(':
                l+=1
            elif ch == ')':
                if l == 0:
                    r +=1
                else:
                    l -=1
        
        self.ans = []
        #dfs(s, 0, l, r)
        bfs(s, l, r)
        return self.ans
        
# @lc code=end

