#
# @lc app=leetcode id=128 lang=python
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #1. O(nlgN), 44ms, sort and check every two elements
        '''
        if not nums:
            return 0
        nums.sort()
        ret = cnt = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                cnt+=1
            #skip if equal to pre val
            elif nums[i] == nums[i-1]:
                continue
            else:
                cnt = 1
            ret = max(ret, cnt)
        return ret
        '''
        #method 2,朴素想法，按照每个数+1,
        #继续递归找下一个数，如果在则继续迭代知道最大值, 即使用hashmap也会TLE
        #算法复杂度time:O(N^3) Space:O(1)
        '''
        tmp = sorted(nums)
        ret_max = 0
        for i, n in enumerate(tmp):
            tmp_cnt = 0
            tmp_val = n
            for x in tmp[i:]:
                if x == tmp_val:
                    tmp_cnt +=1 
                    tmp_val +=1
            ret_max = max(ret_max, tmp_cnt)
        return ret_max 
        '''
        #method 2，开始计数的时候需要满足n-1在序列中,剪纸，但是时间依然很长
        #将list转换成set可以将时间从1560->40ms!!!
        '''
        ret_max = 0
        nums_tmp = set(nums)
        for n in nums:
            if (n-1) in nums_tmp:
                continue
            tmp_val = n
            tmp_cnt = 0
            while tmp_val in nums_tmp:
                tmp_cnt +=1
                tmp_val +=1
            ret_max = max(ret_max, tmp_cnt)
        return ret_max
        '''
        #sort and count,思想：排序，从第二个数开始，如果当前元素减一等于前一个元素，那么序列数目+1，否则reset到1,
        #注意判断有重复数字的情况，需要skip
        #时间复杂度为O(nlogn),排序， 44ms
        '''
        nums_sorted = sorted(nums)
        if len(nums_sorted) <=1:
            return len(nums_sorted)
        pre = nums_sorted[0]
        ret_max = local_max = 1
        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] == pre:
                continue
            if nums_sorted[i] - 1 == pre:
                local_max +=1
                ret_max = max(ret_max, local_max)
            else:
                local_max = 1
            pre = nums_sorted[i]
        return ret_max
        '''
        #method 3, 使用hashmap，hashmap的查找是O(1), 之前一种算法的set复杂度有可能是O(nlog(n)),也有可能是log(n)
        #因此先使用hashmap将整个序列map化，未访问的标记为false,
        #遍历整个数组，当前值为n, 
        # 1.向左遍历，如果hashmap[n-1]存在并且为false，长度+1
        # 2.向右遍历，如果hashmap[n+1]存在并且为fasle,长度+1
        # 更新整个最大长度，遍历结束返回最大长度
        '''
        if len(nums) <= 1:
            return len(nums)
        hashmap = {}
        ret_max =1
        for n in nums:
            hashmap[n] = False
        for n in nums:
            tmp_len = 1
            pre = n -1
            while pre in hashmap and hashmap[pre]== False:
                hashmap[pre] = True
                tmp_len +=1; pre -= 1
            next = n +1
            while next in hashmap and hashmap[next]==False:
                hashmap[next] = True
                tmp_len +=1; next += 1
            ret_max = max(tmp_len, ret_max)
        return ret_max 
        '''

        '''
        #@4 使用hashmap
        if len(nums) <= 1:
            return len(nums)
        hashmap = collections.defaultdict()
        ret = 0
        for n in nums:
            hashmap[n] = False
        for n in nums:
            if n-1 not in hashmap:
                cnt = 1
                next = n+1
                while next in hashmap and hashmap[next] == False:
                    next +=1
                    cnt +=1
                ret = max(ret, cnt)
        return ret
        '''
        #@5, 使用set也很快
        s = set(nums)
        ret = 0
        for n in nums:
            cnt = 1
            if n-1 not in s:
                nxt = n+1
                while nxt in s:
                    nxt +=1
                    cnt +=1
            ret = max(ret, cnt)
        return ret

        

# @lc code=end

