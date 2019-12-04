#
# @lc app=leetcode id=179 lang=python
#
# [179] Largest Number
#

# @lc code=start
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def cmp_fuc(x, y):
            left, right = int(x+y), int(y+x)
            return left - right
        if not nums:
            return ""
        #将a，b拼接成字符串，转换成整型如ab>ba则b要在前面
        cmp_str = [str(n) for n in nums]
        cmp_str.sort(reverse = True, cmp = cmp_fuc)
        if cmp_str[0] == '0':
            return "0"
        else:
            return "".join(cmp_str)
        
# @lc code=end

