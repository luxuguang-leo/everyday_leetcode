#
# @lc app=leetcode id=151 lang=python
#
# [151] Reverse Words in a String
#
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]#reverse all the string
        l = s.split() #split the string with space and store the result in l
        ls = [word[::-1] for word in l] #reverse each word in l and store in ls
        return ' '.join(ls) #join each word and return

        
        

