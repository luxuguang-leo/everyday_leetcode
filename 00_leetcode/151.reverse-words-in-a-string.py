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
        #主要用到了
        # 1.python的切片性质，
        # 2.split函数默认会按照空格，换行，制表符等来切片，
        # 3.join函数的用法
        '''
        s = s[::-1]#reverse all the string
        l = s.split() #split the string with space and store the result in l
        ls = [word[::-1] for word in l] #reverse each word in l and store in ls
        return ' '.join(ls) #join each word and return
        '''
        #如果使用双指针如何做呢？不要用库函数？？
        #use two pointers
        #strip space from left and right
        '''
        l, r = 0, len(s)-1
        while l < r and s[l] == ' ':
            l +=1
        while l < r and s[r] == ' ':
            r -=1
        if l == r:
            if s[r] != " ":
                return s[l]
            else:
                return ""
        if not s[l:r+1]:
            return ""
        s = s[l:r+1]
        s = s[::-1]
        ret, l = [], 0
        pre = s[0]
        for i in range(1, len(s)):
            if s[i] == ' ' and pre != ' ':
                #当前为空格，前一个字符不为空格，[l:i)为有效单词
                tmp = s[l:i]
                ret.append(tmp[::-1])
            elif s[i] != ' ':
                #单词首字母的话，更新l
                if pre == ' ':
                    l = i
                #单词结束
                if i == len(s)-1:
                    tmp = s[l:]
                    ret.append(tmp[::-1])
            pre = s[i]
        return " ".join(ret)
        '''
        #其实不需要对两头进行去空格，只需要记录l， r即可
        s = s[::-1]
        if len(s) <= 1:
            if s == " ":
                return ""
            return s
        l, pre, ret= -1, None, []
        for i in range(len(s)):
            #first time update left boundary
            if s[i] != ' ' and l == -1:
                l = i
            #find valid word in s[l:)
            if s[i] == ' ' and pre and pre != ' ' and l != -1:
                tmp = s[l:i]
                ret.append(tmp[::-1])
            elif s[i] != ' ':
                #find the first character of next word
                if pre and pre == ' ':
                    l = i
                #take care of the case of last word
                if i == len(s) -1 and l != -1:
                    tmp = s[l:]
                    ret.append(tmp[::-1])
            pre = s[i]
        return " ".join(ret)



        
        

