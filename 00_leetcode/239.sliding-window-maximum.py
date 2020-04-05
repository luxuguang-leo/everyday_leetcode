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
        ret = []
        for i in range(len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            if i - q[0] >= k:
                q.popleft()
            if i >= k-1:
                ret.append(nums[q[0]])
        return ret
        #@0301, sliding window,使用一个队列记录窗口内的元素
        #queue的特点是递减，所以要加入队列的时候如果比队尾元素大，则删除队尾，可以保证queue的头是最大的
        #单调递减队列，队头是最大值，队列里面记录的是位置而非值
        '''
        if not nums:
            return []
        q = collections.deque()
        res = []
        for i in range(len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()#q.popleft()
            q.append(i)
            if i - q[0] >= k:
                q.popleft()
            if i >= k -1:
                res.append(nums[q[0]])
        return res 
        '''
