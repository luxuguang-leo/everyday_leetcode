#
# @lc app=leetcode id=84 lang=python
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        #method1,局部峰值，细节问题
        #1.找出序列中局部峰值(不是最后一个数的话比后一个数大，是最后一个数的话不小于前面的数)
        #2.然后往前推，如果数目递减，则求出来面积，更新最大值，否则不计算(图中从1往前到2这一步)
        #最终更新值，时间复杂度为N^2，有可能呢会TLE
        '''
        if not heights:
            return 0
        if len(heights) == 1:
            return heights[0]
        ret = 0
        for i in range(len(heights)):
            if i + 1 < len(heights) and heights[i] <= heights[i+1]:
                continue
            minH = heights[i]
            for j in range(i,-1,-1):
                minH = min(minH, heights[j])
                ret = max(ret, (i-j+1)*minH)
                #print(i, j, ret)
        return ret
        '''
        #利用栈，思想类似于上一个，维持一个单调递增栈(相同元素也要处理)
        #遍历数组，如果大于栈的顶点，则压栈，否则开始计算以栈顶元素(局部最大)往前的所有图形面积
        if not heights:
            return 0
        ret = 0
        #将height补一个0，可以处理最后一个值
        heights.append(0)
        q = list()
        for i in range(len(heights)):
            if not q or heights[i] > heights[q[-1]]:
                q.append(i)
            else:  
                while q and heights[i] <= heights[q[-1]]:
                    h = heights[q[-1]]
                    q.pop()
                    if not q:#最后一个元素
                        w = i
                    else:
                        w = i-q[-1]-1
                    ret = max(ret, h * w)
                q.append(i)
        return ret
            
        
        
# @lc code=end

