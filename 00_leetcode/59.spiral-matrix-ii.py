#
# @lc app=leetcode id=59 lang=python
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        i = j = k = 0
        matrix = [[0] * n for _ in range(n)]
        num =1
        while num <= n*n:
            if i == k and j != n -1 - k:
                matrix[i][j] = num; num +=1
                j +=1
            elif j == n-1-k and i != n -1 -k:
                matrix[i][j] = num; num +=1
                i +=1
            elif i == n-1-k and j != k:
                matrix[i][j] = num; num += 1
                j -=1
            elif j == k and i != k:
                matrix[i][j] = num; num +=1
                i -=1
                if i == k:
                    i +=1; j +=1; k +=1
            else:
                matrix[i][j] = num; num +=1
        return matrix
        
# @lc code=end

