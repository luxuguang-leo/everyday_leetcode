# System Design
## Hash Map

class Item(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap(object):
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return key%self.size

    def set(self, key, value):
        idx = self._hash_function(key)
        for item in self.table[idx]:
            if item.key == key:
                item.value = value
                return
        self.table[idx].append(Item(key, value))

    def get(self, key):
        idx = self._hash_function(key)
        for item in self.table[idx]:
            if item.key == key:
                return item.value
        raise KeyError('Key not found')

    def remove(self, key):
        idx = self._hash_function(key)
        for itemidx, item in enumerate(self.table[idx]):
            if item.key == key:
                del self.table[idx][itemidx]
        raise KeyError('Key not found')



#test case
MyHashTable = HashMap(3)
MyHashTable.set(1, 3)
MyHashTable.set(2, 3)
MyHashTable.set(3, 3)
MyHashTable.set(4, 3)
MyHashTable.set(5, 3)
print(MyHashTable.get(5))
print(MyHashTable.get(1))
print(MyHashTable.get(10))
