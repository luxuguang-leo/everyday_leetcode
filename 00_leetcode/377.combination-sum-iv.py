#
# @lc app=leetcode id=377 lang=python
#
# [377] Combination Sum IV
#

# @lc code=start
class Solution(object):
    def dfs(self, nums, target):
        if target == 0:
            self.cnt +=1
        for i in range(len(nums)):
            if nums[i] > target:
                break
            self.dfs(nums, target-nums[i])
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #DFS TLE
        '''
        nums.sort()
        self.cnt = 0
        self.dfs(nums, target)
        return self.cnt
        '''
        #DP,
        #{1,2,3}, 4
        #{1,2,3}, 3  {1,2,3},2   {1,2,3},1
        #DP[i] = sum(DP(i-nums[i])) 
        '''
        (1, 1, 1, 1)
        (1, 1, 2)
        (1, 2, 1)
        (1, 3)   -> DP[3]
        (2, 1, 1)
        (2, 2)   -> DP[2]
        (3, 1)   -> DP[1]
        '''
        DP = [0] * (target+1)
        DP[0] = 1
        for i in range(1, target+1):
            for n in nums:
                if i >= n:
                    DP[i] += DP[i-n]
        return DP[target]

        
# @lc code=end

