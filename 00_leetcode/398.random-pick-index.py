#
# @lc app=leetcode id=398 lang=python
#
# [398] Random Pick Index
#

# @lc code=start
class Solution(object):
    #蓄水池抽样？？？
    #

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        cnt = 0
        for i in xrange(len(self.nums)):
            if self.nums[i] == target:
                cnt +=1
                if random.randrange(cnt) == 0:
                    ret = i
        return ret


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

