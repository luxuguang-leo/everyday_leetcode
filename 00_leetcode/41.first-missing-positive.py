#
# @lc app=leetcode id=41 lang=python
#
# [41] First Missing Positive
#

# @lc code=start
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #桶排序，大概思路是让对应的index都有对应的值，要不然swap
        #3，4，-1，1按照排序应该是1，-1，3，4，暗含A[A[i]-1]=i
        #如:A[A[0]-1] = A[0]=i+1, A[A[2]-1] = i+1=3
        # ->3， 4， -1， 1
        # -> -1, 4, 3, 1  swap(A[0], A[A[0]-1])
        # -> -1, 1, 3, 4  swap(A[1],A[A[1]-1])
        # -> 1, -1, 3, 4  swap(A[1], A[A[1] -1])
        # -> 1, -1, 3, 4 不变，因为A[i] = i+1, i ==2
        # -> 1, -1, 3, 4 不变，因为A[i] = i+1, i ==3
        #通排序结束之后扫描，第一个非小于0的index+1
        #bucket sort
        #[3, 4. -1, 1]
        #After bucket sort
        #[1, -1, 3, 4]
        #nums[i] = i+1
        '''
        for i in range(len(nums)):
            while  0 < nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        print(nums)
        for i in range(len(nums)):
            if nums[i] != i +1:
                return i+1
        return len(nums)+1
        '''
        i = 0
        while i < len(nums):
            if 0 < nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i+=1
        for i in range(len(nums)):
            if nums[i] != i +1:
                return i+1
        return len(nums)+1
        
# @lc code=end

