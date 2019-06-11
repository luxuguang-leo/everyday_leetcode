#
# @lc app=leetcode id=239 lang=python
#
# [239] Sliding Window Maximum
#
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        if k >= len(nums):
            return nums
        res = []
        dq = collections.deque()
        start = 0
        for ind in range(0, len(nums)):
            if len(dq) == 0:
                dq.append(nums[ind])
            if nums[ind] >= dq[0]:
                dq = [nums[ind]]
            else:
                dq.append(nums[ind])
            if (ind - start+1) >= k:
                res.append(dq[0])
                start += 1
        return res
        

