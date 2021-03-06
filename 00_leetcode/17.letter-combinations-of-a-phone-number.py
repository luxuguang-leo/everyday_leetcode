#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#
class Solution(object):

        
    def dfs(self, digits, pos, path, ret):
        if len(digits) == pos:
            ret.append(path)
            return
        #for i in range(pos, len(digits)):
        #choose each character in num map, 
        #the end is to we have checked all the characters
        for c in self.m[digits[pos]]:
            self.dfs(digits, pos+1, path+c, ret)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        self.m = {'2':['a','b','c'],
                    '3':['d','e','f'],
                    '4':['g','h','i'],
                    '5':['j','k','l'],
                    '6':['m','n','o'],
                    '7':['p','q','r','s'],
                    '8':['t','u','v'],
                    '9':['w','x','y','z']
                    }
        ret = []
        self.dfs(digits, 0, "", ret)
        return ret
        

