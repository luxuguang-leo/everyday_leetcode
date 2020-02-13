#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        '''
        if not matrix:
            return []
        n = len(matrix)
        for i in range(n):
            for j in range(n-i):
                matrix[i][j], matrix[n- 1- j][n- 1 - i] = matrix[n-1-j][n-1-i], matrix[i][j]
        #then flip along x-axias
        for i in range(n//2):
            for j in range(n):
                matrix[i][j], matrix[n-1-i][j] = matrix[n-1-i][j], matrix[i][j]
        '''
        #也可以先对折，再反转
        N = len(matrix)
        for i in range(N):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(N):
            for j in range(N/2):
                matrix[i][j], matrix[i][N-1-j] = matrix[i][N-1-j], matrix[i][j]
        return matrix
        

