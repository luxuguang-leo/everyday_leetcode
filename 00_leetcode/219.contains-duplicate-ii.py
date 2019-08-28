#
# @lc app=leetcode id=219 lang=python
#
# [219] Contains Duplicate II
#
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashTable = {}
        for i in range(len(nums)):
            if nums[i] in hashTable and i - hashTable[nums[i]] <= k:
                return True
            hashTable[nums[i]] = i
        return False

