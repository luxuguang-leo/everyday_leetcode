#
# @lc app=leetcode id=313 lang=python
#
# [313] Super Ugly Number
#

# @lc code=start
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        '''
        ugly_index = [0]*len(primes)
        ret_list = [1]
        while len(ret_list) < n:
            next_val = sys.maxsize
            for i in range(len(primes)):
                next_val = min(next_val, ret_list[ugly_index[i]]*primes[i])
            ret_list.append(next_val)
            for i in range(len(primes)):
                while next_val >= ret_list[ugly_index[i]]*primes[i]:
                    ugly_index[i] +=1

        #print(ret_list)
        return ret_list[-1]
        '''
        #use heap for sorting
        ret = [-1]*n
        ret[0] = 1
        pointN = [0]*len(primes)
        for i in range(1, n):
            min_val = float('inf')
            for j in range(len(primes)):
                min_val = min(min_val, primes[j]*ret[pointN[j]])
            ret[i] = min_val
            for j in range(len(primes)):
                if min_val == primes[j]*ret[pointN[j]]:
                    pointN[j] +=1
        return ret[-1]
            
        

# @lc code=end

