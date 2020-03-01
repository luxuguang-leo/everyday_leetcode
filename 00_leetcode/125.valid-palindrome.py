#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #需要考虑的情况有，如果非字母，非数字，跳过
        #@0301,如果有数字肯定不是回文
        if not s:
            return True
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalpha() and not s[l].isdigit():
                l +=1
            while l < r and not s[r].isalpha() and not s[r].isdigit():
                r -=1
            if s[l].lower() == s[r].lower():
                l +=1
                r -=1
            else:
                return False
        return True
        
# @lc code=end

