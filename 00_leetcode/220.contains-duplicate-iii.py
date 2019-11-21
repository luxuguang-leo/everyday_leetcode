#
# @lc app=leetcode id=220 lang=python
#
# [220] Contains Duplicate III
#

# @lc code=start
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        #brutal force, TLE
        if not nums or k <= 0 or t < 0:
            return False
        '''
        for i in range(len(nums)):
            for j in range(i+1, min(i+k+1, len(nums))):
                if abs(nums[j] - nums[i]) <= t:
                    return True
        return False
        '''
        #2. bisect 
        bst = []
        for i, num in enumerate(nums):
            idx = bisect.bisect_left(bst, num)
            if idx < len(bst) and abs(bst[idx]-num) <= t:
                return True
            if idx > 0 and abs(bst[idx-1] - num) <= t:
                return True
            if i >= k:
                del bst[bisect.bisect_left(bst, nums[i-k])]
            bisect.insort(bst, num)
        return False
        
# @lc code=end

