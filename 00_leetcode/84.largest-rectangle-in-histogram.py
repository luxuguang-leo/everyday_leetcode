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
                continue #这里比较巧妙，如果直接写出判断条件有两种，要么是>下一个元素，或者为数组最后一个元素
            minH = heights[i]
            for j in range(i,-1,-1):
                minH = min(minH, heights[j])
                ret = max(ret, (i-j+1)*minH)#这里没有必要用一个局部变量
        return ret
        '''
        #利用栈，思想类似于上一个，维持一个单调递增栈(相同元素也要处理)
        #遍历数组，如果大于栈的顶点，则压栈，否则开始计算以栈顶元素(局部最大)往前的所有图形面积
        '''
        if not heights:
            return 0
        #将height补一个0，可以处理最后一个值
        heights.append(0)
        s, ret  = [], 0
        for i in range(len(heights)):
            if not s or heights[i] > heights[s[-1]]:
                s.append(i)
            else:  
                while s and heights[i] <= heights[s[-1]]:
                    h = heights[s[-1]]
                    s.pop()
                    if not s:#最后一个元素
                        w = i
                    else:
                        w = i-s[-1]-1
                    ret = max(ret, h * w)
                    #这里面积指什么呢？指以之前栈顶为右边界的矩形面积，左边界不停的向左尝试，知道左边界小于要插入的这个值
                    #高度是每一次的栈顶，右边界为(i-1),左边界为q[-1]，所以面积为h*(i-1 - q[-1])
                s.append(i)
        return ret
        '''
        #可不可以先在栈加入一个-1值，这样就不会为空
        '''
        if not heights:
            return 0
        s, ret = [-1], 0
        heights.append(0)
        for i in range(len(heights)):
            while heights[i] < heights[s[-1]]:
            #这里使用了两个技巧，在原有的bar数组增加一个0
            #在原有的stack提前增加一个-1
            #当s只有一个元素的时候， height[s[-1]] = height[-1] = 0
            #当只有一个元素的时候这个while循环永远不会进入，也就是stack至少有一个元素，永远大于1
                h = heights[s.pop()]
                w = i - 1 - s[-1]
                ret = max(ret, h*w)
            #所以while之外的分支有两种情况进入，1.stack只有一个元素，或者stack内不止一个元素，不过栈顶元素要小于要插入的值
            s.append(i)
        return ret
        '''
        if not heights:
            return 0
        heights.append(0)
        stack, ans = [], 0
        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                tmp = stack.pop()
                h = heights[tmp]
                if not stack:
                    w = i
                else:
                    w = i - stack[-1] -1
                ans = max(ans, h*w)
            stack.append(i)
        return ans
            
        
        
# @lc code=end

