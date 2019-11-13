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
        sum = 0
        for i in nums:
            sum +=i
        return (len(nums)+1)*len(nums)/2-sum
        '''
        ret = 0
        for i in range(len(nums)):
            ret ^= (nums[i] ^ (i+1))
        return ret

# @lc code=end

