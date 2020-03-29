#
# @lc app=leetcode id=376 lang=python
#
# [376] Wiggle Subsequence
#

# @lc code=start
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #DP,或者类似DP，用两个数组标识up和上升的最长长度
        #如果后一个数比前一个数大，则up = down +1
        #否则down = up +1,只能说是DP思想吧
        '''
        N = len(nums)
        if N <=1:
            return N
        up, down = [1]*N ,[1]*N
        for i in range(1, N):
            if nums[i] > nums[i-1]:
                up[i] = down[i-1] +1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                down[i] = up[i-1] +1
                up[i] = up[i-1]
            else:
                down[i] = down[i-1]
                up[i] = up[i-1]
        #print(up, down)
        return max(down[-1], up[-1])
        '''
        #method 空间优化，只需要两个变量保存即可
        '''
        if not nums:
            return 0
        N = len(nums)
        up = down = 1
        for i in range(1, N):
            if nums[i] > nums[i-1]:
                up = down +1
            elif nums[i] < nums[i-1]:
                down = up +1
        return max(down, up)
        '''
        '''
        if not nums:
            return 0
        up = [1]*len(nums)
        down = [1]*len(nums)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up[i] = down[i-1]+1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                up[i] = up[i-1]
                down[i] = up[i-1]+1
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]
        return max(up[-1], down[-1])
        '''
        if not nums:
            return 0
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down+1
            elif nums[i] < nums[i-1]:
                down = up+1
        return max(up, down)
# @lc code=end

