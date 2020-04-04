#
# @lc app=leetcode id=414 lang=python
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #method 1, inefficient
        '''
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        heap = []
        for i in range(len(nums)):
            if len(heap) < 3:
                heapq.heappush(heap, nums[i])
            else:
                heapq.heappushpop(heap, nums[i])
        return heap[0]
        '''
        #method 1, modify, O(n*lg(K), K = 3
        '''
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        #cannot use index in set
        heap = []
        for _ in range(3):
            heapq.heappush(heap, nums.pop())
        while nums:
            heapq.heappushpop(heap, nums.pop())
        return heap[0]
        '''
        #O(N) Time; O(1) Space
        #大概思路，用三个变量保存最大，次大，次次大的值，
        #1.如果大于first, ，可能是最大的数， 错位赋值，first <-val, second <-first, second <- third
        #2.如果大于second小于first，可能是第二大的数，更新second, third
        #3.如果大于third小于second,可能能是第三大的数，只更新third
        #返回third
        #有点类似
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        first = second = third = float('-inf')
        for n in nums:
            if n > first:
                third, second, first = second, first, n
            elif n > second:
                third, second = second, n
            elif n > third:
                third = n
        return third

        
# @lc code=end

