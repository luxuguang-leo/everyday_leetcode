#
# @lc app=leetcode id=38 lang=python
#
# [38] Count and Say
#
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        '''
        if n == 1:
            return '1'
        s = self.countAndSay(n-1)
        ret, cnt = '', 0
        for i in range(len(s)):
            cnt +=1
            if i == len(s)-1 or s[i] != s[i+1]:
                ret += str(cnt)
                ret += s[i]
                cnt = 0
        return ret
        '''
         # 1  ->1
        # 2  ->11
        # 3  ->21
        # 4  ->1211
        # 5  ->111221
        # 6  ->312211
        # 7  ->13112221
        # 8  ->1113213211
        # 9  ->31131211131221
        # 10 ->1321131112311312211
        #找出规律，对每一个字符从头开始
        if n == 1:
            return '1'
        res = "1"
        #for _ in range(1, n):#一共要循环的次数应该是n-1次或者写成
        for _ in range(n-1):
            pre, cnt, new_res = res[0], 0, ""
            #pre用来保留第一个字符为了迭代方便来定义的
            #cnt用来记录其实字符的个数为0
            #new_res用来记录由res生产的新的字符串
            for j in range(len(res)):
                if res[j] == pre:#如果和前一个字符串相同
                    cnt +=1
                else:
                    new_res += str(cnt) + pre
                    cnt = 1
                    pre = res[j]
            res = new_res + str(cnt) + pre
        return res
        

