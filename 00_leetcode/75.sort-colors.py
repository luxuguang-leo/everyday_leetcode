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
        '''
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
        '''
        #method 3
        '''
        if not nums:
            return []
        l = i= 0
        r = len(nums) -1
        while i <=r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l +=1
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -=1
                i -=1#这里需要退后一步
            i+=1
        return nums
        '''
        '''
        if not nums:
            return []
        l = i = 0
        r = len(nums) -1
        while i <= r:
            if nums[i] == 0 and i != l:
                nums[i], nums[l] = nums[l], nums[i]
                l +=1
                i -=1
            elif  nums[i] == 2 and i != r:
                nums[i], nums[r] = nums[r], nums[i]
                r -=1
                i -=1
            i +=1
        return nums
        '''
        #@0301,https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
        #难点在于将整个数组分为四部分，红色(0),白色(1),未排序，蓝色(2)
        #遇到蓝色和红色交互后要不要索引+1?对于红色，交互后当前位置已经就位，要么是1，要么是所以已经排序，+1
        #但对于蓝色，交互后的那个值不确定，所以不能+1
        if not nums:
            return nums
        red = mid = 0
        blue = len(nums) -1
        while mid <= blue:
            if nums[mid] == 2:
                nums[mid], nums[blue] = nums[blue], nums[mid]
                blue -=1
            elif nums[mid] == 0:
                nums[mid], nums[red] = nums[red], nums[mid]
                red +=1
                mid +=1
            else:
                mid +=1
        return nums
        
            

        
# @lc code=end

