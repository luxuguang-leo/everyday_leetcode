#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #copy from right to left
        '''
        l_mn = m + n -1
        l_m = m - 1
        l_n = n -1
        while l_mn >=0 and l_n >=0:
            if l_m >= 0 and nums1[l_m] > nums2[l_n]:
                nums1[l_mn] = nums1[l_m]
                l_m -=1
            else:
                nums1[l_mn] = nums2[l_n]
                l_n -=1
            l_mn -=1
        return nums1
        '''
        i, j = m-1, n -1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[i+j+1] = nums1[i]
                i -=1
            else:
                nums1[i+j+1] = nums2[j]
                j -= 1
        return nums1
            

        
        
        
        
# @lc code=end

