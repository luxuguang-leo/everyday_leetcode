#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        #in place swap 
        '''
        l, r = 0, len(nums) -1
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r], r= nums[r], nums[l], r -1
            else:
                l += 1
        return l
        '''
        #in-place remove
        slow = -1
        for i in range(len(nums)):
            if nums[i] != val:
                slow +=1
                nums[slow] = nums[i]
        return slow+1
        

