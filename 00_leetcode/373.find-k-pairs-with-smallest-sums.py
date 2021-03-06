#
# @lc app=leetcode id=373 lang=python
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        #思路，使用一个小堆，充分利用有序数列性质
        #1.将第一个数组每一个元素分别和第二个数组相加，加入优先队列(和， 第一个元素下标，第二个元素下标)，第一次肯定是顺序的
        #2.取出堆顶最小元素，放入结果中，然后看取出的元素的索引值i, j，因为第一个数组的每一个元素的可能性都已经放在堆中，所以需要
        #在第二个数组中尽可能组合，将(nums[i]+nums[j+1], i, j+1)继续放入堆中
        #循环的结束条件是返回值长度为k
        '''
        if not nums1 or not nums2:
            return []
        ret = []
        heap_list = []
        for j in range(len(nums2)):
            heapq.heappush(heap_list, (nums1[0]+nums2[j], 0, j))
        while len(ret) < min(k, len(nums1)*len(nums2)):
            result, i, j = heapq.heappop(heap_list)
            ret.append([nums1[i], nums2[j]])
            if i +1 < len(nums1):
                heapq.heappush(heap_list, (nums1[i+1] + nums2[j], i+1, j))
        return ret
        '''
        
        #brutal force??
        '''
        if not nums1 or not nums2:
            return []
        ret = []
        min_heap = []
        def push_to_heap(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(min_heap, (nums1[i]+nums2[j], i, j))
        push_to_heap(0,0)
        while len(ret) < min(k, len(nums1)*len(nums2)):
            val, i, j = heapq.heappop(min_heap)
            ret.append([nums1[i], nums2[j]])
            push_to_heap(i, j+1)
            if j == 0:
                push_to_heap(i+1, j)
        return ret
        '''
        #with set to record visited or not, very stright, no trick
        if not nums1 or not nums2:
            return []
        ret, min_heap, visited = [], [], set()
        heapq.heappush(min_heap, (nums1[0]+ nums2[0], (0, 0)))
        visited.add((0, 0))
        while len(ret) < min(k, len(nums1)*len(nums2)):
            _, (i, j) = heapq.heappop(min_heap)
            ret.append([nums1[i], nums2[j]])
            if i+1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(min_heap, (nums1[i+1]+nums2[j], (i+1, j)))
                visited.add((i+1, j))
            if j+1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(min_heap, (nums1[i]+nums2[j+1], (i, j+1)))
                visited.add((i, j+1))
        return ret


        
# @lc code=end

