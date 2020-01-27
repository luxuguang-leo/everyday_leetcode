#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #use default dict 
        hashmap = collections.defaultdict(list)
        for word in strs:
            tmpWord = ''.join(sorted(word))
            hashmap[tmpWord].append(word)
        ret = []
        for v in hashmap.values():
            ret.append(v)
        return ret
            
            
        

