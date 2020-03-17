#
# @lc app=leetcode id=287 lang=python
#
# [287] Find the Duplicate Number
#
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #binary search
        #确定mid,然后扫描所有数组，寻找小于mid的数字的数目，如果cnt小于mid则证明重复数字在[mid,r]内
        '''
        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (r-l)//2 + l
            cnt = 0
            for n in nums:
                if n <= mid:
                    cnt +=1
            if cnt > mid:
                r = mid - 1
            else:
                l = mid + 1
        return l
        '''
        #linked-list cycle
        '''
        slow = nums[0]
        if nums[0] < len(nums):
            fast = nums[nums[0]]
        else:
            return None
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0 #起始位置为0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
        '''
        if not nums:
            return nums
        for n in nums:
            idx = abs(n)
            if nums[idx] < 0:
                return idx
            nums[idx] = -nums[idx]
        return None

        
        




        

