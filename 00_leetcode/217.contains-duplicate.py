#
# @lc app=leetcode id=217 lang=python
#
# [217] Contains Duplicate
#
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        #method 1
        '''
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]] = i
            else:
                return True
        return False
        '''
        # sort and compare

        

