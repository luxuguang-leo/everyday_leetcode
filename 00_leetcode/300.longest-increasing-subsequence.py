#
# @lc app=leetcode id=300 lang=python
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #动态规划方法，f(n)表示以nums[n]为最后一个的最长子序列
        #f(i) = max(f(j)) +1 if nums[j] < nums[i]
        #return dp[-1] 这里不应该返回DP最后一个数，因为DP[i]表示以nums[i]为结尾的最长子序列，
        #不一定所有最长子序列中以nums[i]为结尾是最长的，应该求DP中的最大值,时间复杂度为O(N^2),空间复杂度为O(N)
        #比如
        '''
        if not nums:
            return 0
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            tmpmax = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    tmpmax = max(dp[j]+1, tmpmax)
                dp[i] = tmpmax
        return max(dp)
        '''
        #nlogN ，二分+DP,https://segmentfault.com/a/1190000003819886
        #https://www.youtube.com/watch?v=YoeWZ3ELMEk
        ##NlogN，binary search
        #维持一个递增序列，遍历数组，num[i]
        #1.如果nums[i]大于序列最后最大数，加入序列,这种情况下才有可能让后面的LIS增长，因此整体LIS+1
        #2.如果nums[i]小于最开始的值，替换掉最开始的数,这种情况下不会让隐藏的LIS长度变长，只需替换开始即可
        #3.如果nums[i]位于开头和结尾之间，这种情况需要也同样不会对隐藏的LIS长度有影响，因此需要替换比这个数大的那个数
        #4.注意最终的序列并不是候选的LIS，我们只是维持一个长度等同于LIS的序列，并且有利于后续LIS的方式递增或者维持
        if not nums:
            return 0
        N = len(nums)
        DP = [0]* N
        size = 0
        for n in nums:
            index = bisect.bisect_left(DP, n, 0, size)
            DP[index] = n
            if index == size:
                size +=1
        return size




# @lc code=end

