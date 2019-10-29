#
# @lc app=leetcode id=374 lang=python
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l <= r:
            mid = (r-l)//2 + l
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                r = mid -1
            else:
                l = mid +1
        return l
 
        
# @lc code=end

