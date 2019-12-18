#
# @lc app=leetcode id=331 lang=python
#
# [331] Verify Preorder Serialization of a Binary Tree
#

# @lc code=start
class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        #use stack, if there is 2 '#'s，remove the one before
        #until last, only 1 '#' is left
        p = preorder.split(',')
        stack = []
        for node in p:
            while stack and node == stack[-1] == '#':
                stack.pop()
                if not stack:
                  return False
                stack.pop()
            stack.append(node)
        if len(stack) == 1 and stack[0] == '#':
            return True
        else:
            return False
        
# @lc code=end

