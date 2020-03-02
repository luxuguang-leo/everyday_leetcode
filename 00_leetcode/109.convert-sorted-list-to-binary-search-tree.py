#
# @lc app=leetcode id=109 lang=python
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        dummy = ListNode(-1)
        slow, fast, dummy.next = dummy, head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #slow.next will be the root 
        root = TreeNode(slow.next.val)
        newHead = slow.next.next
        slow.next = None
        root.left = self.sortedListToBST(dummy.next)
        root.right = self.sortedListToBST(newHead)
        return root
        
# @lc code=end

