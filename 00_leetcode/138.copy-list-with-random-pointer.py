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
        '''
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
        '''
        #另外一种方法就是在原节点后面复制，形成一个两倍长的list，然后再更新next和random
        #来处理比较麻烦，好处就是省空间，但是繁琐
        '''
        if not head:
            return None
        #很巧妙的使用hashmap来记录新旧节点之前的对应关系，这样难点在于求新节点的random
        #newNode.random -> 据map找到oldNode -> oldNode.random  -> 据map找到新的节点
        #key:oldNode Value:newNode
        m = {}
        newHead= dummy = Node(-1, None, None)
        oldNode = head
        while oldNode:
            newNode = Node(oldNode.val, None, None)
            newHead.next = newNode
            m[oldNode] = newNode
            newHead = newHead.next
            oldNode = oldNode.next
        oldNode = head
        while oldNode:
            if oldNode.random:
                m[oldNode].random = m[oldNode.random]
            oldNode = oldNode.next
        return dummy.next
        '''
        '''
        if not head:
            return None
        m = {}
        cur = head
        while cur:
            newNode = Node(cur.val, None, None)
            m[cur] = newNode
            cur = cur.next
        m[None] = None#否则在cur.random为空的时候会出错
        cur = head
        while cur:
            m[cur].random = m[cur.random]
            m[cur].next = m[cur.next]
            cur = cur.next
        return m[head]
        '''
        #another solution with O(1) space
        if not head:
            return
        cur = head
        #add copy node
        while cur:
            nxt = cur.next
            NewNode = Node(cur.val)
            cur.next = NewNode
            NewNode.next = nxt
            cur = nxt
        #update random node
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            if cur.next:
                cur = cur.next.next
        #split node into two part
        second = cur = head.next
        while cur and cur.next:
            head.next = cur.next
            head = head.next
            cur.next = head.next
            cur = cur.next
        head.next = None
        return second
        


# @lc code=end

