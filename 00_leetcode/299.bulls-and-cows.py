#
# @lc app=leetcode id=299 lang=python
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        #位置相同，元素相同， bull+1
        #位置不同，元素相同， cow +1
        bull = cow = 0
        hashp = collections.defaultdict(int)
        for i in range(len(secret)):
            s, g = secret[i], guess[i]
            if s == g:
                bull +=1
            else:
                hashp[s] += 1
        for i in range(len(guess)):
            if secret[i] != guess[i] and hashp[guess[i]]:
                cow +=1
                hashp[guess[i]] -= 1
        return str(bull)+'A'+str(cow)+'B'

# @lc code=end

