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
            return ""
        #m = ['..', '.', '']
        sperators = ('..', '.', '')
        stack = []
        for item in path.split("/"):
            if item not in sperators:
                stack.append(item)
            elif item == '..':
                if stack:
                    stack.pop()
        return '/'+'/'.join(stack)
       # @lc code=end

