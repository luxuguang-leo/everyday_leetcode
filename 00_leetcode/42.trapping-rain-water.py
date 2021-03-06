#
# @lc app=leetcode id=42 lang=python
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #1.method
        '''
        if not height:
            return 0
        left, right = [0], []
        tmp_max = 0
        for i in range(1, len(height)):
            tmp_max = max(tmp_max, height[i-1])
            left.append(tmp_max)
        tmp_max = 0
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                right.append(0)
            else:
                tmp_max = max(tmp_max, height[i+1])
                right.append(tmp_max)
        right.reverse()
        ret = 0
        for i in range(len(height)):
            val = min(left[i], right[i]) - height[i]
            if val > 0:
                ret +=val
        return ret
        #2.method
        '''
        #可以直接在这里遍历的时候求出最终结果
        '''
        if not height:
            return 0
        left = [0]
        tmp_max = 0
        for i in range(1, len(height)):
            tmp_max = max(tmp_max, height[i-1])
            left.append(tmp_max)
        max_right, ret = 0, 0
        for i in range(len(height)-2, -1, -1):
            #最右边肯定不会有水
            max_right = max(max_right, height[i+1])
            val = min(left[i], max_right) - height[i]
            if val > 0:
                ret += val
        return ret
        '''
        #优化，使用双指针，两个变量left_max, right_max记录左指针左边最大值，右指针右边最大值
        #如果左最大值小于右最大值，那么左边当前点可以确定，反之右边当前点可以确定
        '''
        if not height or len(height) < 3:
            return 0
        l, r = 0, len(height)-1#从左右倒数第二个数开始算
        l_max, r_max = height[l], height[r]
        ret = 0
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            if l_max <= r_max:
                ret += (l_max - height[l])
                l +=1
            else:
                ret += r_max - height[r]
                r -=1
        return ret
        '''
        #使用单调栈，比较难想，但是想法和84类似，区别在于需要计算盛雨的时候之前应该维护
        #一个单调递减栈
        #如果stack为空，或者height[i] < stack[-1], 入栈
        #否则，出栈，求出width， cur - 1 - s[-1]； 雨水的高度 min(heightRight, heightLeft) - 弹出来的最底的bar
        ans, s = 0, []
        for i in range(len(height)):
            while s and height[i] > height[s[-1]]:
                bottom = s[-1]
                s.pop()
                #if not s:
                    #ans +=0
                #else:
                if s:
                    h = min(height[i], height[s[-1]]) - height[bottom]
                    w = i-1-s[-1]
                    ans += (h*w)
            s.append(i)
        return ans

        
            

            
        
# @lc code=end

