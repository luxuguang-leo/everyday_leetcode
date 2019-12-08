#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #使用最小堆，堆中保留节点值和第条，不停的从取出堆顶，然后根据第几条找出下一个节点然后加入堆中
        dummy = ListNode(-1)
        move = dummy
        minheap = []
        heapq.heapify(minheap)
        N = len(lists)
        for i, l in enumerate(lists):
            if l:heapq.heappush(minheap,(lists[i].val, i))
        while minheap:
            curVal, curIdx = heapq.heappop(minheap)
            curHead = lists[curIdx]
            curNext = curHead.next
            move.next = curHead
            curHead.next = None
            move = curHead
            curHead = curNext
            if curHead:
                lists[curIdx] = curHead
                heapq.heappush(minheap, (curHead.val, curIdx))
        return dummy.next



# @lc code=end
