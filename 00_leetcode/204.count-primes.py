#
# @lc app=leetcode id=204 lang=python
#
# [204] Count Primes
#

# @lc code=start
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        prime = [1]*n
        prime[0]=prime[1] = 0#0-primes
        for i in range(2, n):
            if prime[i] == 1:
                k = i*i
                while k < n:
                    prime[k] = 0
                    k +=i
        #print(prime)
        return prime.count(1)
        
# @lc code=end

