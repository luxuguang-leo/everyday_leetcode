#
# @lc app=leetcode id=268 lang=python
#
# [268] Missing Number
#

# @lc code=start
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        ret = 0
        for i in range(len(nums)):
            ret ^= (nums[i] ^ (i+1))
        return ret
        '''
        return len(nums)*(len(nums)+1)/2 - sum(nums)

# @lc code=end

