#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #brutal soluction O(N^2)
        '''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]
        ''' 


        #use hashtable, k:nums[i], v:i, in python
        # use dict for hashtable, aka, dict = {2:0, 7:1, },
        htable = {}
        for i in range(len(nums)):
            if target - nums[i] in htable:
                return [i, htable[target - nums[i]]]
            else:
                htable[nums[i]] = i
        return [-1, -1]
        
        #O(N)? really but the complexity of dich in Python is O(1) worst is O(N)

