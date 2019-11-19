#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        '''
        #1.hashmap
        hashmap = collections.defaultdict(int)
        for n in nums:
            hashmap[n] +=1
            if hashmap[n] > len(nums)//2:
                return n
        return None
        '''
        #2.sorted
        #return sorted(nums)[len(nums)//2]
        #.moore voting
        maj_idx, cnt = 0, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[maj_idx]:
                cnt +=1
            else:
                cnt -=1
                if cnt == 0:
                    maj_idx = i
                    cnt = 1
        return nums[maj_idx]
# @lc code=end

