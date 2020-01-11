#
# @lc app=leetcode id=39 lang=python
#
# [39] Combination Sum
#
class Solution(object):
    #dfs，并没有传入一个level的变量原因在于最终结果判断结束并没有根据递归层数，全排列需要，
    def dfs(self, nums, target, res, path):
        if target == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            if nums[i] > target:#剪支
                continue
            self.dfs(nums[i:], target - nums[i], res, path+[nums[i]])
    def dfs2(self, nums, target, start, res, path):
        if target == 0:
            res.append(path)
        for i in range(start, len(nums)):
            if nums[i] > target:
                continue
            self.dfs2(nums,target-nums[i], i, res, path+[nums[i]])

    #使用深copy list，和append/pop更直观展示回溯的过程
    def dfs3(self, nums, target, res, path):
        if target == 0:
            res.append(list(path))
        for i in range(len(nums)):
            if nums[i] > target:
                continue
            path.append(nums[i])
            self.dfs3(nums[i:], target - nums[i], res, path)
            path.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #回溯，核心:加入决策路径，选择回溯列表
        if not candidates:
            return []
        res = []
        #self.dfs(candidates, target, res, [])
        #self.dfs2(candidates, target, 0, res, [])
        self.dfs3(candidates, target, res, [])
        return res

