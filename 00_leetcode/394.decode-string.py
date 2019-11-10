#
# @lc app=leetcode id=394 lang=python
#
# [394] Decode String
#

# @lc code=start
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #可以用一个stack或者两个stack，
        #1.遇到数字计算数字
        #2.遇到[ 压stack,将数字和string
        #3.遇到] 弹stack,得到数字和之前的string,当前string按照数字重复后和之前string累计
        #4.遇到一般字符，更新当前string
        #'''
        stack = []
        curnum = 0
        curstr = ''
        for ch in s:
            if ch.isdigit():
                curnum = curnum*10 +int(ch)
            elif ch == '[':
                stack.append(curstr)
                stack.append(curnum)
                curnum = 0
                curstr = ''
            elif ch == ']':
                prenum = stack.pop()
                prestr = stack.pop()
                curstr = prestr + prenum*curstr
            else:
                curstr += ch
        return curstr
        '''
        s_num, s_str = [], []
        curnum = 0
        cur_str = ''
        for ch in s:
            if ch.isdigit():
                curnum = curnum*10 +int(ch)
            elif ch == '[':
                s_num.append(curnum)
                s_str.append(cur_str)
                curnum = 0
                cur_str = ''
            elif ch == ']':
                prenums = s_num.pop()
                prestr = s_str.pop()
                #while prenums > 0:
                cur_str = prenums*cur_str
                    #prenums -=1
                cur_str = prestr + cur_str
            else:
                cur_str += ch
        return cur_str
        '''




        # @lc code=end

