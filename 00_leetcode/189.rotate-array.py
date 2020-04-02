#
# @lc app=leetcode id=189 lang=python
#
# [189] Rotate Array
#
class Solution(object):
    def helper(self, nums):
        mid , l = (len(nums) + 1)//2, len(nums) -1
        for i in range(mid):
            nums[i], nums[l-i] = nums[l-i], nums[i]
        return nums
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        if not nums:
            return
        n = len(nums)
        k = k % n
        nums[:n-k] = self.helper(nums[:n-k])
        nums[n-k:] = self.helper(nums[n-k:])
        nums[:] = self.helper(nums[:])
        return nums
        '''
        '''
        #method 2, cyclic swap
        k = k % len(nums)
        for i in range(len(nums)):
            start = i
            while True:
                next = (start + k) % len(nums)
                nums[next], nums[start] = nums[start], nums[next]
                start = next
                if start == i:
                    break
        start += 1
        '''
        #https://www.cnblogs.com/grandyang/p/4298711.html
        if not nums or k%(len(nums)) == 0:
            return nums
        idx, start, cur =0, 0, nums[0]
        for _ in range(len(nums)):
            pre = cur
            idx = (idx+k)%len(nums)
            cur = nums[idx]
            nums[idx] = pre
            if idx == start:
                start +=1
                idx = start
                cur = nums[idx]
        return nums



        

        

