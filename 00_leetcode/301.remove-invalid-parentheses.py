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
        self.ans = set()
        self.min_removed = float('inf')
        
        def dfs(index, left, right, removed, cur):
            if index == len(s):
                if left == right:
                    if removed < self.min_removed:
                        self.min_removed = removed
                        self.ans = {cur}
                    elif removed == self.min_removed:
                        self.ans.add(cur)
            else:
                if s[index] != '(' and s[index] != ')':
                    dfs(index+1, left, right,removed, cur+s[index])
                else:
                    dfs(index+1, left, right, removed+1, cur)
                    if s[index] == '(':
                        dfs(index+1, left+1, right, removed, cur+'(')
                    elif s[index] == ')' and right < left:
                        dfs(index+1, left, right+1, removed, cur+')')
        dfs(0,0,0,0, "")
        return list(self.ans)

        
# @lc code=end

