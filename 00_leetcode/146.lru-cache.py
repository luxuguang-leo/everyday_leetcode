#
# @lc app=leetcode id=146 lang=python
#
# [146] LRU Cache
#

# @lc code=start

class Node(object):
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            n = self.dict[key]
            self._delete(n)
            self._insert(n)
            return n.value
        #not found
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            #remove first it
            self._delete(self.dict[key])
        n = Node(key, value)
        self._insert(n)
        self.dict[key] = n
        if len(self.dict) > self.capacity:
            n = self.head.next
            self._delete(n)
            del self.dict[n.key]
    #delete the node n
    def _delete(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        
        
    #insert from tail    
    def _insert(self, node):
        p = self.tail.prev
        p.next = node
        
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    #another version is to insert from the head
    '''
class Node(object):
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        

    def insert(self, node):
        #insert from the head
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node
        
    def delete(self, node):
        #delete node
        pre = node.prev
        next = node.next
        pre.next = next
        next.prev = pre
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            #在字典中，取出值
            #放在对头
            n = self.dict[key]
            self.delete(n)
            self.insert(n)
            return n.val
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            #删除这个值
            self.delete(self.dict[key])
        n = Node(key, value)
        self.insert(n)
        self.dict[key] = n
        if len(self.dict) > self.capacity:
            #缓存溢出，找到队列尾部，删除之
            node = self.tail.prev
            self.delete(node)
            del self.dict[node.key]

    '''

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

