#
# @lc app=leetcode id=91 lang=python
#
# [91] Decode Ways
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #DP类似于跳台阶， DP[i] = DP[i-1] + DP[i-2]
        #如果  int(s[i-1:i]) == 0, 那么如果前面数字为1，2 =>  DP[i] = DP[i-2] 
        #如果  10 < int(s[i-2:i]） <=26 且 ！= 20
        #否则  DP[i] = DP[i-2]
        '''
        if not s:
            return 0
        DP = [0]*(len(s)+1)
        DP[0] = 1
        if s[0] == '0':
            DP[1] = 0
        else:
            DP[1] = 1
        for i in range(2, len(s)+1):
            if s[i-1] == '0':
                if s[i-2] not in ["1", "2"]:
                    return 0
                else:
                    DP[i] += DP[i-2]
            else:
                if 10 < int(s[i-2:i]) <= 26:
                    DP[i] = DP[i-1] + DP[i-2]
                else:
                    DP[i] += DP[i-1]
        return DP[-1]
        '''
        #第一次写的比较啰嗦，其实通项公式是:
        #DP[i] = DP[i-1] if s[i-1] != '0'
        #      + DP[i-2] if 9 < s[i-2:i] < 27
        DP = [0] * (len(s) +1)
        DP[0] = 1
        if s[0] == '0':
            DP[1] = 0
        else:
            DP[1] = 1
        for i in range(2, len(s)+1):
            if 10 <= int(s[i-2:i]) <= 26 and s[i-1] != '0':
                DP[i] = DP[i-1] + DP[i-2]
            elif int(s[i-2:i]) == 10 or int(s[i-2:i]) == 20:
                DP[i] += DP[i-2]
            elif s[i-1] != '0':
                DP[i] += DP[i-1]
            else:
                return 0
        return DP[-1] 
        
# @lc code=end

