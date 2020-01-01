#
# @lc app=leetcode id=215 lang=python
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution(object):
    import heapq
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #use nlargest
        '''
        k_larget = heapq.nlargest(k, nums)
        return k_larget[-1]
        '''
        #use heappush and heappop
        '''
        min_heap = []
        for n in nums:
            heapq.heappush(min_heap, n)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return heapq.heappop(min_heap)
        '''
        #simplify 
        if not nums:
            return None
        min_heap = []
        for n in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
            else:
                heapq.heappushpop(min_heap, n)
        return min_heap[0]
        
# @lc code=end

