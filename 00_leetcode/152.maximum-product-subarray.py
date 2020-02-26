#
# @lc app=leetcode id=152 lang=python
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        if not nums:
            return 0
        N = len(nums)
        min_nums = [0]*N
        max_nums = [0]*N
        global_max = min_nums[0]=max_nums[0] = nums[0]
        for i in range(1, N):
            max_nums[i] = max(max_nums[i-1]*nums[i], min_nums[i-1]*nums[i], nums[i])
            min_nums[i] = min(min_nums[i-1]*nums[i], max_nums[i-1]*nums[i], nums[i])
            global_max = max(max_nums[i], global_max)
        return global_max
        '''
        '''
        if not nums:
            return 0
        max_global = min_pre = max_pre = nums[0]
        for i in range(1, len(nums)):
            f, m = min_pre, max_pre
            max_pre = max(m *nums[i], f*nums[i], nums[i])
            min_pre = min(f*nums[i], m*nums[i], nums[i])
            max_global = max(max_pre, max_global)
        return max_global
        '''
        '''
        if not nums:
            return
        local_min = [0]*len(nums)
        local_max = [0]*len(nums)
        global_max = local_min[0] = local_max[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                #负数使的大数变小，小数变大
                local_min[i] = min(nums[i], local_max[i-1]*nums[i])
                local_max[i] = max(nums[i], local_min[i-1]*nums[i])
            else:
                local_min[i] = min(nums[i], local_min[i-1]*nums[i])
                local_max[i] = max(nums[i], local_max[i-1]*nums[i])
            global_max = max(global_max, local_max[i])
        return global_max
        '''
        if not nums:
            return
        global_max = nums[0]
        local_min_pre = local_min = nums[0]
        local_max_pre = local_max = nums[0] 
        for i in range(1, len(nums)):
            if nums[i] < 0:
                #负数使的大数变小，小数变大
                local_min = min(nums[i], local_max_pre*nums[i])
                local_max = max(nums[i], local_min_pre*nums[i])
            else:
                local_min = min(nums[i], local_min_pre*nums[i])
                local_max = max(nums[i], local_max_pre*nums[i])
            global_max = max(global_max, local_max)
            local_max_pre = local_max
            local_min_pre = local_min
        return global_max

# @lc code=end

