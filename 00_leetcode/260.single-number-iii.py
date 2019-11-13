#
# @lc app=leetcode id=260 lang=python
#
# [260] Single Number III
#

# @lc code=start
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #想法比较难想到，主要利用亦或性质n^n=0的性质，
        #和之前找出不同的一个数的区别在于有两个，然后我们想利用这个规律，只需要找出两个数不同的那一个bit位，然后就可以将整个数组
        #分成两组，分别用之前的解法就行，找出的这一个bit位
        xor = 0
        for n in nums:
            xor ^= n
        left, right = 0, 0
        cnt = 0
        while xor & 1 == 0:
            xor >>=1
            cnt +=1
        xor = 1<< cnt
        for n in nums:
            if n&xor == 0:
                left ^= n
            else:
                right ^= n
        return [left, right]


# @lc code=end

