#
# @lc app=leetcode id=448 lang=python
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #same as LC41, find the first positive
        '''
        if not nums:
            return []
        ret = []
        for i in range(len(nums)):
            while nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i],nums[nums[i]-1]
        for i in range(len(nums)):
            if nums[i] != i+1:
                ret.append(i+1)
        return ret
        '''
        #只需要标记可以在正确位置的数即可
        #与LC442稍微不同的是需要两次扫描数组，因为不能一次解决
        #LC442使用映射，可以在第二次找到重复的数
        #LC448第一次标记，第二轮找出正值
        #如[4 3 2 7 8 2 3 1]->
        #[-4 -3 -2 -7 8 2 -3 -1]
        #然后遍历发现8， 2这两个值为正，意味着原本应该是5，6的并没有被映射
        ret = []
        for i in range(len(nums)):
            idx = abs(nums[i])-1
            nums[idx] = -abs(nums[idx])
        for i in range(len(nums)):
            if nums[i] > 0:
                ret.append(i+1)
        return ret
        '''


        
        
# @lc code=end

