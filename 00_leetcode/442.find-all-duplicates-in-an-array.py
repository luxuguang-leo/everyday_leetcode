#
# @lc app=leetcode id=442 lang=python
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #标记法，
        if not nums:
            return []
        ret = []
        for n in nums:
            idx = abs(n)-1
            if nums[idx] < 0:
                ret.append(abs(n))
            else:
                nums[idx] = -nums[idx]
        return ret

        #method 1,使用如LC41,in-place交换的办法，将需要的数字交换到正确的位置上
        '''
        if not nums:
            return nums
        for i in range(len(nums)):
            while nums[i] != i +1 and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        ret = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                ret.append(nums[i])
        return ret
        '''
        #method 2, 其实没必要交互排序，只需要将可以放在合适位置的数标记即可
        '''
        ret = []
        for i in range(len(nums)):
            idx = abs(nums[i]) -1
            if nums[idx] < 0:
                ret.append(abs(nums[i]))
            else:
                nums[idx] = - nums[idx]
        return ret
        #'''
        
# @lc code=end

