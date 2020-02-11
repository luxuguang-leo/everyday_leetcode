#
# @lc app=leetcode id=367 lang=python
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        #[l,r]区间
        l, r = 0, num
        while l <= r:
            mid = l + (r-l)//2
            val = mid * mid
            if val == num:
                return True
            elif  val > num:
                r = mid -1
            else:
                l = mid + 1
        return False
        
# @lc code=end

