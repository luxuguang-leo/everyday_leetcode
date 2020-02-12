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
        '''
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
        '''
        if not nums:
            return []
        #从后往前找到第一个非递增的数作为要替换的位置
        i = len(nums)-1
        while i > 0 and nums[i] <= nums[i-1]:
            i -=1
        #got i,注意，这里i-1才是不满足条件的下标而不是i
        if i == 0:
            #return nums[::-1]
            return nums.reverse()
        #找到真实的下标
        i -= 1
        #找到后半部分最接近nums[i]且比nums[i]大的那一个值
        #这里隐含了右半部分其实是一个有从后序递增序列，只需要从后往前找到第一个比nums[i]即可
        index = len(nums) - 1
        while index > i and nums[index] <= nums[i]:
            index -=1
        nums[i], nums[index] = nums[index], nums[i]
        nums[i+1:] = sorted(nums[i+1:])#之前优化过的，因为i之后的即使交换了也是递减序列，所以反转就得到递增序列
        return nums
        

        
# @lc code=end

