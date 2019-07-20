#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        #use sliding window, two pointers, and 
        #left = 0
        #hashtable, hashtable{'a':0, 'b':1, 'c':2}
        #max_len = i - left
        left = max_len = 0
        hTable = {}
        for i in range(len(s)):
            if s[i] in hTable and left <= hTable[s[i]]:
                left = hTable[s[i]] + 1
            else:
                max_len = max(max_len, i - left +1)
            hTable[s[i]] = i
        return max_len
        #sliding window, but little hard to image

        '''
        错误点在于
        1.更新窗口的时候，abc之后，来了一个‘a’，这个时候需要将left往右移动一位而不是直接移动到再次出现‘a’的位置，
        2.然后所有每次操作都需要更新最大长度，是当前位置-left +1，记得要加1
        3.hashtable保存的是字符和出现的位置，只是用来判断有误重复用，hashtable并没有特别之处
        '''
        

