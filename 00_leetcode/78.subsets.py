#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#
class Solution(object):
    def dfs(self, nums, res, path):
        res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], res, path+[nums[i]])
   
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        #for those backtracking problems
        #https://leetcode.com/problems/subsets/discuss/429534/General-Backtracking-questions-solutions-in-Python-for-reference-%3A
        res = []
        self.dfs(nums, res, [])
        return res
        '''
        #使用bit manipulation
        #所有的组合有2^N种组合，N为数组长度，如果数组的每一个元素用1代表取，0代表不取，很容易得到一个二进制和最终结果的对应如下
        #   abc         subset
        #   000         {}
        #   001         {c}
        #   010         {b}
        #   011         {bc}
        #   100         {a}
        #   101         {ac}
        #   110         {ab}
        #   111         {abc}
        #是不是很容易写出来呢？时间复杂度为2^N * len(nums)
        ret = []
        for i in range(1<<len(nums)):#一共有2^N种组合
            tmp = []
            for j in range(len(nums)):
                #这里有多种做法，我的做法是i右移j位然后看是0还是1
                #if((i >> j) & 0x01):
                #也可以1左移j位置，然后与i与
                if i & (1<<j):
                    tmp.append(nums[j])
            ret.append(tmp)
        return ret



