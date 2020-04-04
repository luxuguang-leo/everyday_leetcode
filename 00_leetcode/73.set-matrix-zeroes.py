#
# @lc app=leetcode id=73 lang=python
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """


        #使用第一行，第一列来标志对应的这一行需要是否需要被清零
        m, n = len(matrix), len(matrix[0])
        firstRowZero = 0
        firsetColZeros = 0
        for i in range(m):
            
        '''
        #O(M+N), 使用两个数组来记录需要更新的行，列
        m, n = len(matrix), len(matrix[0])
        m_rows, n_cols = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    m_rows.add(i); n_cols.add(j)
        for row in m_rows:
            matrix[row]= [0 for _ in range(n)]
        for col in n_cols:
            for row in matrix:
                row[col] = 0
            #for i in range(m):
                #matrix[i][col] = 0
        return matrix
        '''
        '''
        #使用第一行，第一列来用作之前的m， n的数组，使用两个变量标记第一行，第一列需不需要更新为0
        m, n = len(matrix), len(matrix[0])
        firstRowZero, firstColZero = 1, 1
        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = 0
                break
        for j in range(n):
            if matrix[0][j] == 0:
                firstRowZero = 0
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if firstColZero == 0:
            for col in matrix:
                col[0] = 0
        if firstRowZero == 0:
            for i in range(n):
                matrix[0][i] = 0
        return matrix
        '''
# @lc code=end

