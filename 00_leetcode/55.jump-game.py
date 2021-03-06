#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#

# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #greedy，原题并不是求恰好到达i点,只求能否达到i点，并且i点在最大跳数之内，所以只要从前往后递推，i+g[i] >大于之前的距离就更新，否则不更新
        '''
        if len(nums) <=1:
            return True
        reach = 0
        for i in range(len(nums)):
            if i > reach or reach > len(nums)-1:
                break
            reach = max(reach, i + nums[i])
            i +=1
        return reach >= len(nums)-1
        '''
        if len(nums) <=1:
            return True
        reach = 0
        for i in range(len(nums)):
            reach = max(reach, i + nums[i])
            if reach < i+1:
                return False
            if reach >= len(nums)-1:
                return True
        return True




        
        
# @lc code=end

