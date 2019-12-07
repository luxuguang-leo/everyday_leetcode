'''
This questions is locked, but very common for sliding window, so I add it manually. Question:
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: tis "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: tis "aabbb" which its length is 5.

'''

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
    """
    :type s: str
    :rtype: int
    """
    '''
    思路，sliding window,题目要求出最多包含两个元素的最长子串，在往右滑动后，查看当前map的种类，大于2则从左往
    '''
    m = collections.defaultdict(int) 
    l = ret = 0
    for i in range(len(s)):
        m[s[i]] += 1
        while len(m) > 2:
            m[s[l]] -=1
            l +=1
            if m[s[l]] == 0:
                del m[s[l]]
        ret = max(ret, i -l +1)
    return ret
        
    def lengthOfLongestSubstringKDistinct(self, s, k):
    '''
    如果将两个元素改为k个元素
    '''
    if k < 0:
        return 0
    m = collections.defaultdict(int)
    l = ret = 0
    for i in range(len(s)):
        m[s[i]] +=1
        while len(m) > k:
            m[s[l]] -=1
            l +=1
            if m[s[l]] == 0:
                del m[s[l]]
        ret = max(ret, i-l+1)
    return ret
    
    
