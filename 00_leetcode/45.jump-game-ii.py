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
        #贪心算法，每走一步比较下一步能走的最远距离是多少，最终结果在最先到达的距离里面
        #然后在下一步最远之间都要更新最远距离
        pre_max_reach = cur_max_reach = 0
        cnt = i = 0
        while cur_max_reach < len(nums)-1:
            while i <= pre_max_reach:
                cur_max_reach = max(cur_max_reach, i+nums[i])
                i +=1
            if cur_max_reach == pre_max_reach:
                return -1
            pre_max_reach = cur_max_reach
            cnt +=1
        return cnt
                



        
# @lc code=end

