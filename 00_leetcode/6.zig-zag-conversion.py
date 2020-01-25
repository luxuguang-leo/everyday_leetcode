#
# @lc app=leetcode id=6 lang=python
#
# [6] ZigZag Conversion
#
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        #对于第一行和最后一行，interval = 2n-2
        #对于中间行，间隔分别为 interval - 2*i, 2*i
        '''
        if not s or numRows == 0:
            return ""
        if numRows == 1:
            return s
        l = len(s)
        interval = 2*numRows -2
        ret = ''
        row = 0
        for i in range(row, l, interval):
            ret += s[i]
        for row in range(1, numRows-1):
            inter = 2 * row
            j = row
            while j < l:
                ret += s[j]
                inter = interval - inter
                j = j + inter
                
        for i in range(numRows-1, l, interval):
            ret += s[i]
        return ret
        '''
        if numRows <= 1:
            return s
        index, step = 0, 1
        lines = [""]*numRows
        for ch in s:
            lines[index] += ch
            index += step
            if index ==0 or index == numRows -1:
                step *= -1
            '''
            if(index == 0):
                step = 1
            if(index == numRows - 1):
                step = -1
            '''
        return "".join(lines)
                    

