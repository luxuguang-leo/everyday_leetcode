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

