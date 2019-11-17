#
# @lc app=leetcode id=381 lang=python
#
# [381] Insert Delete GetRandom O(1) - Duplicates allowed
#

# @lc code=start
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = list()
        self.dict = collections.defaultdict(set)
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        ret = False
        if val in self.dict:
            ret = True
        self.dict[val].add(len(self.list))
        self.list.append(val)
        
        
    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            return False
        if not self.dict[val]:
            return False
        idx, last = self.dict[val].pop(), self.list[-1]
        self.list[idx] = last
        self.dict[last].add(idx)
        self.dict[last].discard(len(self.list)-1)
        self.list.pop()
        return True
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.list)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

