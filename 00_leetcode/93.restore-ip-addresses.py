#
# @lc app=leetcode id=93 lang=python
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution(object):
    def dfs(self, s, ret, path):
        #剪纸，当剩余的s长度已经尝过还需要的ip长度时直接返回不需要再次DFS， brilliant
        if len(s) > 12 - len(path)*3:
            return
        #终止条件，string是剩下的字符串
        if not s and len(path) == 4:
            ret.append(".".join(path))
            return ret
        for i in range(1, 4):
            if len(s) < i:
                continue#如果剩余的字符长度小于取得子串，证明取的太长了，不可以
            num = int(s[:i])#这里如果i==0,则int(空串)报错，应该
            #str(num) == str[:i]剔除掉例如01 001 这种情况的case
            if num <= 255 and str(num) == s[:i]: 
                self.dfs(s[i:], ret, path+[s[:i]])
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        #DFS,大概思路没获取两个或者三个字符就进行一次DFS
        if not s or len(s) > 12:
            return []
        ret = []
        self.dfs(s, ret, [])
        return ret
        
# @lc code=end

