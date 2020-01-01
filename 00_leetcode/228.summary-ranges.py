#
# @lc app=leetcode id=228 lang=python
#
# [228] Summary Ranges
#

# @lc code=start
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        def append_str(l, r):
            if l == r:
                return str(l)
            else:
                return str(l)+'->'+str(r)
        if not nums:
            return []
        ret, start, i = [], 0, 0
        while i < len(nums) -1:
            if nums[i]+1 != nums[i+1]:
                ret.append(append_str(nums[start], nums[i]))
                start = i+1
            i +=1
        ret.append(append_str(nums[start], nums[i]))
        return ret

        
# @lc code=end

