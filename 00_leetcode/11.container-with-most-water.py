#
# @lc app=leetcode id=11 lang=python
#
# [11] Container With Most Water
#
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #first brutal algo, O(N^2)
        '''
        max_volum = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                max_volum = max(max_volum, (j-i)* min(height[j],height[i]))
        return max_volum
        '''
    
        #use two pointers
        max_volum, head, tail = 0, 0, len(height) -1
        while head < tail:
            max_volum = max(max_volum, (tail - head)* min(height[head], height[tail]))
            if height[head] < height[tail]:
                head += 1
            else:
                tail -= 1
        return max_volum
        


