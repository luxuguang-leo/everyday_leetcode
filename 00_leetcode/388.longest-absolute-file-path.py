#
# @lc app=leetcode id=388 lang=python
#
# [388] Longest Absolute File Path
#

# @lc code=start
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        #使用栈，
        #用分隔符'\n'找出目录文件，
        #对每一个目录文件，使用\t统计深度
        #栈，记录当前深度和对影深度的最长path值
        #有几种情况需要考虑
        #1/当前目录文件深度<=栈顶的深度，表示需要处理的层数目录是比较少的，需要会退到比较少的层次来计算当前层次
        stack = [(-1,0)]
        input_new = input.split("\n")
        max_len = 0
        for p in input_new:
            depth = p.count('\t')
            p = p.replace('\t','')
            while stack and depth <= stack[-1][0]:
                stack.pop()
            if '.' in p:#处理文件
                max_len = max(max_len, stack[-1][1]+len(p))
            else:
                stack.append((depth, stack[-1][1] + len(p)+1))
        return max_len

        
# @lc code=end

