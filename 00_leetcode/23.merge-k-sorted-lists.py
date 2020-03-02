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
        minheap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minheap, (lists[i].val, i))
        dummy = ListNode(-1)
        move = dummy
        while minheap:
            #取出堆中的最小值，找到第几个list，然后取出list的头，然后断开之前的连接
            #然后顺序访问list，往后取，并且更新小堆，直到堆为空
            curListVal, curIdx = heapq.heappop(minheap)
            curHead = lists[curIdx]
            curNext = curHead.next
            move.next = curHead
            curHead.next = None
            move = move.next
            if curNext:
                lists[curIdx] = curNext
                heapq.heappush(minheap, (curNext.val, curIdx))
        return dummy.next
# @lc code=end

