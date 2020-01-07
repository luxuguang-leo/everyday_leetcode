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
        q = collections.deque()
        i, res = 0, []
        for i in range(len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            if i - q[0] == k:
                q.popleft()
            if i >= k -1:
                res.append(nums[q[0]])
        return res 
