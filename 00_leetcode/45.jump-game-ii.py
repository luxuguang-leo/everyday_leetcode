#
# @lc app=leetcode id=45 lang=python
#
# [45] Jump Game II
#

# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = cnt = pre = pos = 0
        while cur < len(nums)-1:
            cnt +=1
            pre = cur
            while pos <= pre:
                cur = max(pos+nums[pos], cur)
                pos +=1
        return cnt



        
# @lc code=end

