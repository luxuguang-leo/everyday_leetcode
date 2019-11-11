#
# @lc app=leetcode id=264 lang=python
#
# [264] Ugly Number II
#

# @lc code=start
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        #维护三个指针，分别表示通过x2, x3, x5得到下一个丑数的指针
        #1.下一个丑数从，当前数乘以三个指针的最小值来
        #2. 如果发现下一个数比三个指针的乘数的值要大，下一个指针+1
        #有点DP的味道
        '''
        new_2, new_3, new_5 = 0, 0, 0
        ugly_list = [1]
        while len(ugly_list) < n:
            ng = min(ugly_list[new_2]*2, ugly_list[new_3]*3, ugly_list[new_5]*5)
            ugly_list.append(ng)
            while ng >= ugly_list[new_2]*2:
                new_2 += 1
            while ng >= ugly_list[new_3]*3:
                new_3 +=1
            while ng >= ugly_list[new_5]*5:
                new_5 +=1
        return ugly_list[-1]
        '''
        #heapq，将元素放进去，然后遍历，分别乘以2,3,5，取最小值，与堆顶比较，如果小于堆订就更新
        heap_list = [1]
        while len(heap_list) < n:
            for i in range(len(heap_list)):
                ng = min(heap_list[i]*2, heap_list[i]*3, heap_list[i]*5)
                if ng <= heap_list[0]:
                    heapq.heappush(ng)
        return heap_list[-1]


        
# @lc code=end

