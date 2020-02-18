#
# @lc app=leetcode id=228 lang=python
#
# [228] Summary Ranges
#

# @lc code=start
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        def convert2str(l, r):
            if l > r:
                return ""
            elif l == r:
                return str(l)
            else:
                return str(l)+"->"+str(r)
        if not nums:
            return []
        start = i = 0
        end = len(nums)-1
        ret = []
        while i < end:
            #tmp = []
            if nums[i]+1 != nums[i+1]:
                ret.append(convert2str(nums[start], nums[i]))
                start = i+1
            i+=1
        ret.append(convert2str(nums[start], nums[i]))
        #最终退出的时候i==len(nums)-1
        #考虑两种情况，1.如果最后一个和之前是连续的，那么start为之前的一个数
        #2.如果最后一个数不是连续的，那么start同样也是之前的一个数，没有差别
        return ret
# @lc code=end

