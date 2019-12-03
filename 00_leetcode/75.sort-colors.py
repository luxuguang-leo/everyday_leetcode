#
# @lc app=leetcode id=75 lang=python
#
# [75] Sort Colors
#

# @lc code=start
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #method 1,one pass counting numbers
        #2.two pass, replace original array with counted 
        if not nums:
            return []
        '''
        n1 = n2 = n3 = 0
        for n in nums:
            if n == 0:
                n1 += 1
            elif n == 1:
                n2 += 1
            elif n == 2:
                n3 +=1
        for i in range(len(nums)):
            if i < n1:
                nums[i] = 0
            elif i < n1 + n2:
                nums[i] = 1
            else:
                nums[i] = 2
        return nums
        '''
        #method,头尾两个指针，red指针和blue指针
        red = i = 0
        blue = len(nums)-1
        while i <= blue:
            if nums[i] == 0:
                nums[red], nums[i] = nums[i], nums[red]
                red +=1
            if nums[i] == 2:
                nums[blue], nums[i] = nums[i], nums[blue]
                blue -=1
            else:
                i +=1
        
            

        
# @lc code=end

