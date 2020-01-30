#
# @lc app=leetcode id=165 lang=python
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        #1
        '''
        if not version1 or not version2:
            return -1
        str1 = version1.split('.')
        str2 = version2.split('.')
        #when both str1 and str2 have the same length and have the same value
        while len(str1)  or len(str2) :
            if len(str1) == 0:
                str1 = '0'
            if len(str2) == 0:
                str2 = '0'
            if int(str1[0]) > int(str2[0]):
                return 1
            elif int(str1[0]) < int(str2[0]):
                return -1
            else:
                str1 = str1[1:]
                str2 = str2[1:]
        return 0
        '''
        #2
        str1 = version1.split('.')
        str2 = version2.split('.')
        delta = len(str1) - len(str2)
        if delta > 0:
            str2 += ['0']*delta
        elif delta < 0:
            str1 += ['0']*(-delta)
        for i in range(len(str1)):
            if int(str1[i]) > int(str2[i]):
                return 1
            elif int(str1[i]) < int(str2[i]):
                return -1
        return 0
        
        
# @lc code=end

