#
# @lc app=leetcode id=134 lang=python
#
# [134] Gas Station
#

# @lc code=start
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        #比较不好想，需要只遍历一次，所以如果刚开始不能出发，需要记录
        #差多少燃料，如果最终剩余的燃料数大于等于这个差的燃料数目
        #则证明到达最后一个点后继续走之前的那段是可以形成闭环的
        #1.总的加油量必须大于等于总的耗油量
        #2.如果当前剩余油量为负值，证明从之前某点开始不满足条件，需要从下一个点开始
        startidx = 0
        total = sum = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            sum += gas[i] - cost[i]
            if sum < 0:
                startidx = i +1
                sum = 0
        if total >= 0:
            return startidx
        else:
            return -1
        #total表示从开始点，剩余的油量，如果不足也记录为负数，到最终结束作为是否满足的条件
        #sum表示从预设的起始点出发到现在点消耗的油量，如果遇到为负的情况，表明之前的判断不对，需要更新到下一个点
        #
             
# @lc code=end

