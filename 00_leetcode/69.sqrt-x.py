#
# @lc app=leetcode id=69 lang=python
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #use binary search
        l, r= 0, x
        while l <= r:
            mid = l + (r-l)/2
            val = mid * mid
            if val == x:
                return mid
            elif val > x:
                r = mid - 1
            else:
                l  = mid + 1
        return r
        
# @lc code=end

