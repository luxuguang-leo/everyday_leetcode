#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return None
        nums.sort()
        ret = []
        #after sorting, use two pointers, O(N^2)
        for i in range(len(nums) - 2):
            start, end = i + 1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while start < end:
                val = nums[i] + nums[start] + nums[end]
                if  val == 0:
                    ret.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start] == nums[start +1]:
                            start += 1
                    while start < end and nums[end] == nums[end-1]:
                            end -= 1
                    start +=1
                    end -=1
                elif val < 0:
                    start += 1
                else:
                    end -= 1
        return ret

