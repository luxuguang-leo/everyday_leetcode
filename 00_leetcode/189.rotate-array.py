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
        '''
        k, l = k % len(nums), len(nums)
        cnt = 0#total in all we need to move l steps
        for i in range(l):
            cur_idx = i
            cur_val = nums[i]
            loop_start = False
            while not loop_start or i != cur_idx:
                loop_start = True
                next_idx = (cur_idx + k) % l
                next_val = nums[next_idx]
                nums[next_idx] = cur_val
                cur_idx = next_idx
                cur_val = next_val
                cnt += 1
                if cnt == l:
                    return
        '''
        k, l = k % len(nums), len(nums)
        cnt = 0
        for i in range(l):
            cur_idx = i
            cur_val = nums[i]
            while True:
                next_idx = (cur_idx + k) % l
                next_val = nums[next_idx]
                nums[next_idx] = cur_val
                cur_idx = next_idx
                cur_val = next_val
                cnt += 1
                if cur_idx == i:
                    break
            if cnt == l:
                return
     

