#
# @lc app=leetcode id=334 lang=python
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #这种方法其实只是寻找整个序列中的值，但是最终的first second 以及返回True的时候序列不代表最终的三元组
        #但是是work的，理由是当返回真的时候，证明前面至少有两个值比当前小
        '''
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
        '''
        #2.使用LIS的二分法
        if len(nums) < 3:
            return False
        array = []
        for n in nums:
            idx = bisect.bisect_left(array, n)
            if idx == len(array):
                array.append(n)
            else:
                array[idx] = n
            if len(array) >=3:
                return True
        return False
        
# @lc code=end

