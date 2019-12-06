l#
# @lc app=leetcode id=30 lang=python
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []
        #sliding window方法，没有想到窗口大小，根据题意窗口大小应该是N*len(words[0])
        #然后按照这么大的固定窗口来滑动，匹配每一个len(word)大小的单词是否出现在map中
        #1.如果出现，将临时map更新，并比较和原始map是否小于等于，大于则不满足
        #2.如果不出现则继续滑动
        m = collections.Counter(words)
        w = len(words[0])
        #hash_s = {}
        window_size = w*len(words)
        if len(s) < window_size:
            return []
        ret = []
        for i in range(len(s)-window_size +1):
            hash_s = {}
            for j in range(0, window_size+1, w):#这里应该注意j的边界，并且根据j break时候的值判断有没有还整个window来匹配
                sub_str = s[i+j:i+j+w]
                #print("now",j, i, sub_str)
                if sub_str in m:
                    hash_s[sub_str] = hash_s.get(sub_str, 0) +1
                    #print(sub_str,hash_s[sub_str], i, j)
                    if hash_s[sub_str] > m[sub_str]:
                        break
                else:
                    break
            #print("loop once", j)
            if j == window_size:
                ret.append(i)
        return ret


        
# @lc code=end

