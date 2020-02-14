#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        m, n = len(matrix), len(matrix[0])
        i = j = level = 0
        ret = []
        while len(ret) < m*n:
            if i == level and j != n - 1 - level:
                ret.append(matrix[i][j])
                j +=1
            elif j == n-1-level and i != m-1-level:
                ret.append(matrix[i][j])
                i +=1
            elif i == m-1-level and j != level:
                ret.append(matrix[i][j])
                j -=1
            elif i != level and j == level:
                ret.append(matrix[i][j])
                i -=1
                if i == level:
                    i +=1
                    j +=1
                    level +=1
            else:
                ret.append(matrix[i][j])
            #if len(ret) == m*n:
                #return ret
        return ret
                
        
# @lc code=end

