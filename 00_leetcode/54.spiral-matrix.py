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
        i = j = k = 0#level k
        row, col = len(matrix), len(matrix[0])
        res = []
        while True:
            if i == k and j != col - 1 - k:
                res.append(matrix[i][j])
                j += 1
            elif j == col -1 -k and i != row - 1 - k:
                res.append(matrix[i][j])
                i += 1
            elif i == row - 1 - k and j != k:
                res.append(matrix[i][j])
                j -= 1
            elif i != k and j == k:
                res.append(matrix[i][j])
                i -= 1
                if i == k:
                    i += 1
                    j += 1
                    k += 1
            else:
                res.append(matrix[i][j])
            if len(res) == row*col:
                return res
            

