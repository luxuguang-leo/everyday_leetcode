#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not numbers:
            return []
        l, r = 0, len(numbers)-1
        for i in range(len(numbers)):
            #固定一个值，在后续数列中寻找差值
            l, r = i+1, len(numbers)-1
            m_target = target - numbers[i]
            while l <= r:
                mid = l + (r-l)//2
                if m_target == numbers[mid]:
                    return [i+1, mid+1]
                elif m_target < numbers[mid]:
                    r = mid -1
                else:
                    l = mid +1
            #return []#这里对每一个i值要判断，不应该在这里返回，因为后续的numbers[i]有可能是解
            
        
# @lc code=end

