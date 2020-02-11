#
# @lc app=leetcode id=349 lang=python
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        '''
        return list(set(nums1) & set(nums2))
        '''
        #1.hashmap
        #2.sort and compare
        #return set(nums1)& set(nums2)
        '''
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()
        i = j = 0
        ret = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ret.append(nums1[i])
                i +=1
                j +=1
            elif nums1[i] < nums2[j]:
                i +=1
            else:
                j+=1
        return set(ret)
        '''
        #hashmap
        if not nums1 or not nums2:
            return []
        ret, m = [], collections.defaultdict(int)
        for n1 in nums1:
            m[n1] +=1
        for n2 in nums2:
            if n2 in m:
                ret.append(n2)
        return set(ret)
            
            
        

        
# @lc code=end

