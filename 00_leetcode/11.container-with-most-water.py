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
        #use very intuitative idea
        #1.the widest is canditate 
        #2.Shorten the width, but we should choose a large one beween first and last
        #3.end of the loop is the width is 0
        if not height:
            return 0
        s, e = 0, len(height)-1
        max_water = 0
        while s < e:
            max_water = max(max_water, (e-s)*min(height[s], height[e]))
            if height[s] < height[e]:
                s +=1
            else:
                e -=1
        return max_water
        


