#
# @lc app=leetcode id=71 lang=python
#
# [71] Simplify Path
#

# @lc code=start
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path:
            return None
        stack = []
        path_new = path.split("/")
        for c in path_new:
            if not c or c == '.':
                continue
            if c == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return '/'+'/'.join(stack)


        
# @lc code=end

