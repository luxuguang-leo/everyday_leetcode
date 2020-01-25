#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#
class Solution(object):
    def dfs(self, digits, index,path, ret):
        if index == len(digits):
            ret.append(path)
            return
        for letter in self.m[digits[index]]:
            #choose one and move to next character
            self.dfs(digits, index+1, path+letter,ret)

        
        
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
        

