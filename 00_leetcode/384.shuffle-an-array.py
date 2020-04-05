#
# @lc app=leetcode id=384 lang=python
#
# [384] Shuffle an Array
#

# @lc code=start
class Solution(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        '''
        nums = self.nums[:]#copy
        random.shuffle(nums)
        return nums
        '''
        #洗牌算法
        #1.k个元素，选取[0,k)范围内随机数m
        #2交换n[0], n[m]
        #在[1,k)，也就是剩下的范围内按照1，2来运行
        _nums = self.nums[:]
        l = len(_nums)
        for i in range(l):
            #randint和randrange区别在于randint右边界是包含的，randrange是可以增加步长的
            m = random.randint(i, l-1)
            #m = random.randrange(i, l)
            _nums[i], _nums[m] = _nums[m], _nums[i]
        return _nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

