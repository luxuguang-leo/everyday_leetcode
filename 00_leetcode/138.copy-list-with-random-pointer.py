#
# @lc app=leetcode id=138 lang=python
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        #空间换时间，用一个hash记录新旧节点，然后在生成新的list之后，按照map，
        #索引map的value的random
        #map{old_node_1:new_node_1, ...,old_node_n:new_node_n}
        #map[old_node_1].random=map[old_node_1.random]
        '''
        if not head:
            return None
        dummy = Node(0, None, None)
        hash_map = dict()
        hash_map[head] = dummy
        new_head, point = dummy, head
        while point:
            node_new = Node(point.val, point.next, None)
            hash_map[point] = node_new
            new_head.next = node_new
            new_head,point = new_head.next, point.next
        node = head
        while node:
            if node.random:
                hash_map[node].random = hash_map[node.random]
            node = node.next
        return dummy.next
        '''
        #简便写法
        if not head:
            return None
        hash_map = dict()
        node = head
        while node:
            new_node = Node(node.val, node.next, 0)
            hash_map[node] = new_node
            node = node.next
        hash_map[None] = None
        node = head
        while node:
            hash_map[node].random = hash_map[node.random]
            hash_map[node].next = hash_map[node.next]
            node = node.next
        return hash_map[head]
        #另外一种方法就是在原节点后面复制，形成一个两倍长的list，然后再更新next和random
        #来处理比较麻烦，好处就是省空间，但是繁琐

# @lc code=end

