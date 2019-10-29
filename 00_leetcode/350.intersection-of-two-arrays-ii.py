#
# @lc app=leetcode id=350 lang=python
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict_table = {}
        res = []
        for n in nums1:
            dict_table[n] = dict_table.get(n, 0) + 1
        for n in nums2:
            if n in dict_table and dict_table[n] > 0:
                res.append(n)
                dict_table[n] -=1
        return res
# @lc code=end

