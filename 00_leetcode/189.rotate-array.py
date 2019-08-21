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
        #method 1
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
        #method 2, cyclic replacement
        k = k % len(nums)
        cnt, start = 0, 0
        while cnt < len(nums):
            cur = start
            pre = nums[start]
            while True:
                nxt = (cur + k) % len(nums)
                nums[cur], nums[nxt] = nums[nxt], nums[cur]
                cur = nxt
                cnt += 1

                if start == cur:
                    break


            start += 1




        

        

