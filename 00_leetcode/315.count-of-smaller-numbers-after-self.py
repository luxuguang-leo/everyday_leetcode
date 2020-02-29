#
# @lc app=leetcode id=315 lang=python
#
# [315] Count of Smaller Numbers After Self
#

# @lc code=start
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        #TLE
        if not nums:
            return []
        ret = [0]*len(nums)
        for i in range(len(nums)):
            cnt = 0
            for n in nums[i+1:]:
                if n < nums[i]:
                    cnt +=1
            ret[i] = cnt
        return ret
        '''
        #二分,从后往前，比较难想
        ret, sorted_array = [], []
        for i in range(len(nums)-1, -1, -1):
            pos = bisect.bisect_left(sorted_array, nums[i])
            ret.append(pos)
            #bisect.insort_left(sorted_array, nums[i])
            sorted_array.insert(pos, nums[i])
        return ret[::-1]

# @lc code=end

