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
        #理解题意，前m n个都是拍好序的，而且nums1足够长，可以从num1, nums2后往前比较,谁大就放在n+m-1位置
        i = m - 1
        j = n - 1
        while j >= 0:
            if i >=0 and nums1[i] > nums2[j]:
                nums1[i+j+1] = nums1[i]
                i -= 1
            else:
                nums1[i+j+1] = nums2[j]
                j -= 1
        
        
        
        
# @lc code=end

