#
# @lc app=leetcode id=162 lang=python
#
# [162] Find Peak Element
#

# @lc code=start
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1 2 3 4 5 4 3 2 1
        '''
        | 1 | 2 | 3 | 4 | 5 | 4 | 3 | 2 | 1 |
        |---|---|---|---|---|---|---|---|---|
        | l | _ | _ | _ | m | _ | _ | _ | r |
        a[m] > a[m+1] -> r=m (Not m-1 since m is larger and it itself can be the answer)
        | 1 | 2 | 3 | 4 | 5 | 4 | 3 | 2 | 1 |
        |---|---|---|---|---|---|---|---|---|
        | l | m | _ | _ | r | X | X | X | X |

        a[m] < a[m+1] -> l = m+1 (Since m is smaller than m+1, m will for sure be not the answer)
        | 1 | 2 | 3 | 4 | 5 | 4 | 3 | 2 | 1 |
        |---|---|---|---|---|---|---|---|---|
        | X | X | l | m | r | X | X | X | X |

        a[m] < a[m+1] -> l = m+1 (Since m is smaller than m+1, m will for sure be not the answer)
        | 1 | 2 | 3 | 4 | 5   | 4 | 3 | 2 | 1 |
        |---|---|---|---|-----|---|---|---|---|
        | X | X | X | X | l,r | X | X | X | X |

        l is the answer

        '''
        '''
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] < nums[mid+1]:
                l = mid +1
            elif nums[mid] > nums[mid+1]:
                r = mid
        return l
        '''
        #收缩条件可是意识num[mid]与num[mid+1]比较，然后用开区间来处理，知道最终l==r,返回这个l
        if not nums:
            return -1
        l, r = 0, len(nums) -1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] < nums[mid+1]:
                l = mid +1
            elif nums[mid] > nums[mid+1]:
                r = mid
        return l
        

       # @lc code=end

