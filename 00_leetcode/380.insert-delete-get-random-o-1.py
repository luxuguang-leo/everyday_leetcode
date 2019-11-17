#
# @lc app=leetcode id=380 lang=python
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
class RandomizedSet(object):
    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()
        self.size = 0

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.set:
            self.set.add(val)
            self.size +=1
            return True
        else:
            return False
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.set:
            return False
        else:
            self.set.remove(val)
            self.size -=1
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        ind = random.randint(0, self.size - 1)
        return list(self.set)[ind]  
    '''


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = list()
        self.dict = dict()
       

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            self.list.append(val)
            self.dict[val] = len(self.list)-1
            return True
        else:
            return False
        
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            idx, last = self.dict[val], self.list[-1]
            self.list[idx]=last
            self.dict[last]=idx
            self.list.pop()
            self.dict.pop(val,0)
            return True
        else:
            return False
    

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randint(0, len(self.list) - 1)
        return self.list[idx]
       

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

