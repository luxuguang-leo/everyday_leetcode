#
# @lc app=leetcode id=658 lang=python
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        #@0229
        #O(n), two-pointers
        '''
        while len(arr) > k:
            if x - arr[0] <= arr[-1] - x:
                arr.pop()
            else:
                arr.pop(0)
        return arr
        '''
        #method, heapify
        if x < arr[0]:
            return arr[:k]
        elif x > arr[-1]:
            return arr[-k:]
        else:
            l, r = 0, len(arr) - k
            while l < r:
                mid = l + (r-l)//2
                if x - arr[mid] > arr[mid+k] - x:
                    l = mid +1
                else:
                    r = mid
            return arr[l:l+k]


        
# @lc code=end

