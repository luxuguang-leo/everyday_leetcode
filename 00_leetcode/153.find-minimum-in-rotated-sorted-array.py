#
# @lc app=leetcode id=153 lang=python
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        l, r = 0, len(nums)-1
        while l < r:
            mid = (r-l)//2 + l
            if nums[mid] > nums[r]:
                l = mid +1
            else:
                r = mid
        return nums[l]
        #don't know why failed???
        #判断有问题，比如4 5 6 7 0 1 2
        #l   r   mid  n[mid] nu[l]  nu[r]
        #0   6   3     7      5        2    n[mid]> n[l]  n[m]>n[r] [4,6]
        #4   6   5     1      0        2    n[mid] > n[l] n[m] < n[r]
        #这个时候两种算法就出现问题了，正确的是如果小于右边界，那么将确定右边界
        #而错误算法这时候的左边界其实就是最小值，但是中间值大于左边界就取右半部分丢失了可能包含
        #最小值的情况，所以不对
        '''
        while l < r:
            mid = (r-l)//2 + l
            if nums[mid] > nums[l]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
        '''
 # @lc code=end

