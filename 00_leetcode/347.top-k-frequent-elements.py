#
# @lc app=leetcode id=347 lang=python
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #先统计次数，放到hashmap中，然后对次数进行heapify,输出key值即可
        '''
        hashmap = collections.Counter(nums)
        ret_list = []
        for key, cnt in hashmap.items():
            if len(ret_list) < k:
                heapq.heappush(ret_list, (cnt, key))
            else:
                if ret_list[0][0] < cnt:
                    heapq.heappop(ret_list)
                    heapq.heappush(ret_list, (cnt, key))
                    #heapq.heapreplace(ret_list, (cnt, key))
        return [x[1] for x in ret_list]
        '''
        if not nums:
            return []
        m = collections.Counter(nums)
        heap = []
        for key, cnt in m.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt, key))
            else:
                if cnt > heap[0][0]:#need update if cur cnt is larger
                    heapq.heappushpop(heap, (cnt, key))
        return [x[1] for x in heap]


        

        
# @lc code=end

