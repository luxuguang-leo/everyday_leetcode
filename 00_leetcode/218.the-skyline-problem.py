#
# @lc app=leetcode id=218 lang=python
#
# [218] The Skyline Problem
#

# @lc code=start
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        #1.将矩形拆解为两个端点并标记，
        #2.按照x轴排序
        #3.维持一个max_heap，刚开始是0
        #4.依次扫描各顶点，出现以下情况：
        #5.1 Innode,加入大堆，比较堆顶和preheight的值，堆顶代表画笔当前高度，如果出现高度差，则更新结果
        #5.2 Outnode,从大堆中删除，比较堆顶和preheight的值，
        if not buildings:
            return buildings
        new_building = []
        for l, r, h in buildings:
            new_building += [(l, -h), (r, h)]
        new_building.sort()
        result, max_heap = [], [0]
        prev = max_heap[0]
				
        # Save the heights that will be removed later
        to_remove = collections.defaultdict(int)
        for x, h in new_building:
            if h < 0:
                heapq.heappush(max_heap, h)
            else:
                to_remove[-h] += 1
            # Remove heights if they become the root of the heap
            while to_remove[max_heap[0]] > 0:
                to_remove[max_heap[0]] -= 1
                heapq.heappop(max_heap)           
            cur = max_heap[0]
            if cur != prev:
                result.append((x, -cur))
                prev = cur
        
        return result







        
# @lc code=end

