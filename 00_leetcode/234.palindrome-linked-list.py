#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #really easy?find the half point and reverse the other part, compare if there are the same
        '''
        if not head or not head.next:
            return True
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        newPart = self.reverseList(slow)
        slow = head
        while newPart and slow:
            if newPart.val != slow.val:
                return False
            slow = slow.next
            newPart = newPart.next
        return True
        '''
        #use stack
        '''
        if not head or not head.next:
            return True
        stack = []
        fast = slow = head
        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        if fast:
            slow = slow.next
        while slow and stack:
            if slow.val != stack.pop():
                return False
            slow = slow.next
        return True
        '''
        '''
        #如何才能忽略奇偶长度呢？找到的中间点有可能是奇数点，也有可能是偶数点
        #翻转后后半部分要么比前半部分多一个节点，要么等于前一个节点长度，不比较最后一个即可
        if not head or not head.next:
            return True
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #slow.next应该是分割点
        node, second = None, slow.next
        slow.next = None #加不加都可以，不断开的话前面的list会很长
        while second:
            next = second.next
            second.next = node
            node, second = second, next
        while node and head:
            if node.val != head.val:
                return False
            head = head.next
            node = node.next
        return True
        '''
        #注意处理奇有两种做法，之前的做法是slow向前移动一步
        #现在的做法是stack把当前结点再多压入一次
        if not head or not head.next:
            return True
        stack, slow, fast = [], head, head
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        if fast and not fast.next:#处理奇数结点情况，slow为分界点
            stack.append(slow.val)
        while slow and stack:
            if slow.val != stack.pop():
                return False
            slow = slow.next
        return True

        
# @lc code=end

