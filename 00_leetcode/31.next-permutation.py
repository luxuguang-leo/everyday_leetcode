#
# @lc app=leetcode id=31 lang=python
#
# [31] Next Permutation
#

# @lc code=start
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #1  2   4   6  5  3 
        #step.1, 从右往左，找到第一个不满足递减序列的元素， i = 2, 4
        #step.2, 在刚才的右半部分找到比4大的第一个数，这个数是比4稍微大的点的数，
        #step.3, 交换两个数 -> 1  2   5    6  4   3
        #step.4，将i的右半部分排序即可得到结果-> 1  2   5    3   4   6
        #step.5,注意第一步的corner case，如果全是递降序列，则全部逆序即可
        if not nums:
            return []
        i = j = len(nums) -1
        while i > 0 and nums[i-1] >= nums[i]:
            i -=1
        if i == 0:
            nums.reverse()
            return 
        idx = i -1 #the actual num to not ascending
        while j > idx:
            if nums[j] > nums[idx]:
                break
            j -= 1
        nums[idx], nums[j] = nums[j], nums[idx]
        l, r = idx +1, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1; r -=1
        return nums

        
# @lc code=end

