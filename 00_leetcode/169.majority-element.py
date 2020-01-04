#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        '''
        #1.hashmap
        hashmap = collections.defaultdict(int)
        for n in nums:
            hashmap[n] +=1
            if hashmap[n] > len(nums)//2:
                return n
        return None
        '''
        #2.sorted
        #return sorted(nums)[len(nums)//2]
        #.moore voting
        '''
        maj_idx, cnt = 0, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[maj_idx]:
                cnt +=1
            else:
                cnt -=1
                if cnt == 0:
                    maj_idx = i
                    cnt = 1
        return nums[maj_idx]
        '''
        #3 bit manuplicate，比较难想啊，对每一个bit,记录所有数组的此bit位的1的个数，如果1的个数大于
        #len/2，则此bit应该标记为1，否则为0
        if not nums:
            return None
        L = len(nums)
        ret = 0
        for i in range(32):
            ones = 0
            for n in nums:
                if ones > L//2:
                    break
                if(n & (1<<i) != 0):
                    ones +=1
            if ones > L//2:
                if i == 31:
                    ret = -((1<<31) - ret)
                else:
                    ret |= (1<<i)
            #print(i, ones,ret)
        
        return ret

# @lc code=end

