#
# @lc app=leetcode id=136 lang=python
#
# [136] Single Number
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #O(n) memory
        '''
        nc = collections.Counter(nums)
        for n in nc:
            if nc[n] == 1:
                return n
        '''
        #O(1) memory
        tmp = 0
        for n in nums:
            tmp = tmp ^ n
        return tmp

        
# @lc code=end

