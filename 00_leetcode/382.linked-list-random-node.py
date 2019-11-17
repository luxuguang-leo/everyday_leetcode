#
# @lc app=leetcode id=382 lang=python
#
# [382] Linked List Random Node
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        ret = self.head.val
        node = self.head
        cnt = 0
        while node:
            cnt +=1
            if random.randrange(cnt) == 0:
                ret = node.val
            node = node.next
        return ret



        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

