#
# @lc app=leetcode id=60 lang=python
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        num_str = [str(x) for x in range(1, 10)]
        res = ''
        fact = [1]*n
        for i in range(1, n):
            fact[i] *= fact[i-1]*i
        k -= 1
        for i in range(n, 0, -1):
            first = k // fact[i-1]
            k %= fact[i-1]
            res += num_str[first]
            num_str.pop(first)
        return res
        
        
# @lc code=end

