#
# @lc app=leetcode id=85 lang=python
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution(object):
    '''
    def maxArea(self, height):
        if not height:
            return 0
        ret = 0
        stack = list()
        height.append(0)
        for i in range(len(height)):
            if not stack or height[i] > height[stack[-1]]:
                stack.append(i)
            else:
                while stack and height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    if not stack:
                        w = i
                    else:
                        w = i - stack[-1] - 1
                    ret = max(ret, w*h)
                stack.append(i)
        return ret
    '''
    def maxArea(self, height):
        if not height: return 0
        ret, s = 0, [-1]
        height.append(0)
        for i in range(len(height)):
            while height[i] < height[s[-1]]:
            #参考LC84
                h = height[s.pop()]
                w = i-1-s[-1]
                ret = max(ret, h*w)
            s.append(i)
        return ret
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        r, c = len(matrix), len(matrix[0])
        height = [0]*c
        ret = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            ret = max(ret, self.maxArea(height))
        return ret
                    
        
# @lc code=end

