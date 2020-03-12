#
# @lc app=leetcode id=387 lang=python
#
# [387] First Unique Character in a String
#
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #hashmap, stupid question
        '''
        hashTable = {}
        for ch in s:
            if ch not in hashTable:
                hashTable[ch] = 1
            else:
                hashTable[ch] += 1
        for i in range(len(s)):
            if hashTable[s[i]] == 1:
                return i
        return -1
        '''
        #one-pass soluction, use map and dict
        #@0312,使用dict记录次数，使用队列将出现一次的元素放入，如果发现大于1，则出队
        hashTable = {}
        q = collections.deque()
        for idx, ch in enumerate(s):
            hashTable[ch] = hashTable.get(ch, 0) +1
            if hashTable[ch] == 1:
                q.append((ch, idx))
            while q and hashTable[q[0][0]] > 1:
                q.popleft()
        if not q:
            return -1
        else:
            return q[0][1]

        

