#
# @lc app=leetcode id=491 lang=python
#
# [491] Increasing Subsequences
#

# @lc code=start
class Solution(object):
    def dfs(self, nums, ret, path):
        if len(path) >= 2 and path not in ret:
            ret.append(path[:])
        visited = {}
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] in visited:
                continue
            visited[nums[i]] = True
            if not path or nums[i] >= path[-1]:
                path.append(nums[i])
                self.dfs(nums[i+1:], ret, path)
                path.remove(nums[i])

    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #backtracking 效率最低
        '''
        if len(nums) < 3:
            return []
        ret = []
        self.dfs(nums, ret, [])
        return ret
        '''
        #https://buptwc.com/2018/07/03/Leetcode-491-Increasing-Subsequences/
        #使用字典，记录以每一个位置的递增子序列
        d = collections.defaultdict(list)
        for i in range(len(nums)):
            d[i].append([nums[i]])
        #d = {i:[[nums[i]]] for i in range(len(nums))}
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] >= nums[j]:
                    for l in d[j]:
                        d[i].append(l+[nums[i]])
        
        s = set()
        res = []
        for i in range(len(nums)):
            for l in d[i]:
            	# 因为字典中本身存在长度为1的list，需要我们排除
                if len(l) < 2: continue
                if tuple(l) in s: continue
                s.add(tuple(l))
                res.append(l)
        return res

        
# @lc code=end

