#
# @lc app=leetcode id=295 lang=python
#
# [295] Find Median from Data Stream
#

# @lc code=start
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.large = []
        self.small = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.large) == 0:
            heapq.heappush(self.large, -num)
            return 
        if num <= -self.large[0]:
            heapq.heappush(self.large, -num)
        else:
            heapq.heappush(self.small, num)
        #keep balance
        if len(self.large) - len(self.small) == 2:
            #move one element to small heap
            heapq.heappush(self.small, -heapq.heappop(self.large))
        elif len(self.small) - len(self.large) == 2:
             #move one element to large heap
            heapq.heappush(self.large, -heapq.heappop(self.small))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return (-self.large[0]+self.small[0])/2.0
        elif len(self.large) > len(self.small):
            return -self.large[0]
        else:
            return self.small[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

