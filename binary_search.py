#patton 1, standard
#搜索区间是[left, right], while l <= r 的中止条件是left = Right + 1,区间就是[Right +1 , Right]
#右区因为已经判断过了nums[mid]元素，所以需要再除掉mid元素的 [left, mid-1] 或者 [mid + 1, right]来搜索

#目标，在有序的nums数组中，需要target的下标，找到返回其下标，没找到就返回-1
def binaySearch(nums, target):
    if not nums:
        return -1
    l, r = 0, len(nums)-1           #代表了边界的下标，第一个0， 最后一个len(nums)-1
    while l <= r:                   #中止条件就是l = r +1, 这时候l已经越界了，区间为[r+1, r]
        mid = (r-l)//2 + l
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:    #如果目标值小于中间元素值，表明右边界应该不是mid，减一，mid-1
            r = mid -1
        elif target > nums[mid]:    #如果目标值大于中间元素，表明左边界应该不是mid，加一，mid+1
            l = mid +1
    return -1

#patten 2
#这个算法用来求区间左边界，也就是第一个出现target的左边界, 这个的思路就是不停的向右收缩
def binarySearchLeftBoundary(nums, target):
    if not nums:
        return -1
    l, r = 0 , len(nums)            #开区间搜索，左边界为[0, len(nums))
    while l < r:                    #循环中止条件就是l == r,也就是[r, r)
        mid = (r-l)//2 + l
        if target == nums[mid]:
            right = mid
        elif target < nums[mid]:    #如果目标值小于中间值，那么右区间有可能是mid,因为是开区间，所以r=mid
            r = mid
        elif target > nums[mid]:    #如果目标值大于中间值，那么左区间需要往右扩展，因为左边是闭区间，所以l=mid+1
            l = mid + 1
    if left == len(nums):           #推出的条件有可能是等于r，如果l搜索到了序列的最后一个表明整个序列都没有找到，返回-1
        return -1
    if nums[left] == target:        #这种情况下找到一个左边界，应该是第一个左边界为target的下标
        return left
    else:
        return -1                   #否则也是没有找到

    ##闭区间的写法
def binartSearchLeftBoundary(nums, target):
    if not nums:
        return -1
    l, r = 0, len(nums)-1
    while l <= r:
        mid = l + (r-l)//2
        if target == nums[mid]:
            r = mid-1
        elif target < nums[mid]:
            r = mid -1
        elif target > nums[mid]:
            l = mid +1
    if l >= len(nums) or nums[l] != target: #找不到条件是l已经超出了数组范围，或者nums[l]并不是需要找的值
        return -1
    return l

#patten 3
#寻找区间右边界，也就是出现target的最后一个值，也就是右边界

def binarySearchRightBoundary(nums, target):
    if not nums:
        return -1
    l, r = 0, len(nums)
    while l < r:                    #退出条件是l==r, 搜索的区间为[l, r)
        if target = nums[mid]:      #如果找到一个值，将左边界继续往前多试探一部
            l = mid + 1
        elif target < nums[mid]:    #如果目标值小于中间值，那么确定右边界
            r = mid
        elif target > nums[mid]:    #如果目标值大于中间值，那么左边界更细为mid+1
            l = mid +1
    if left == 0:
        return -1
    return left -1                  #如果推出则返回试探的值-1

    ##闭区间写法
    def binartSearchRightBoundary(nums, target):
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if target == nums[mid]:
                l = mid +1
            elif target > nums[mid]:
                l = mid +1
            elif target < nums[mid]:
                r = mid -1
        #这里需要检查右边界越界的情况
        if r < 0 or nums[r] != target:
            return -1
        return right



例子：
#1.标准二分  [1, 3, 6, 8, 10]  target = 8
target  l   r   mid    action 
8       0   4    2      target > nums[mid]
8       3   4    3     target == nums[mid] ->返回3


#2.1 使用开区间，寻找左边界  [1, 2, 2, 2, 3, 4, 5, 7] target = 2
target  l   r   mid     action
2       0   8   4       target < nums[mid] -> r = mid 
2       0   4   2       target == nums[mid] -> r = mid = 2
2       0   2   1       target == nums[mid] -> r = mid = 1
2       0   1   0       target > nums[mid]  -> l = mid +1 = 1 -> l == r 循环条件推出
这时候l = r = 1   l就是满足等于2的左边边界

#2.2 使用闭区间，寻找左边界  [1, 2, 2, 2, 3, 4, 5, 7] target = 2
target  l   r   mid     actions
2       0   7   3       target == nums[mid] -> r = mid -1
2       0   2   1       target == nums[mid] -> r = mid -1 = 0 
2       0   0   0       target > nums[mid]  -> l = mid +1 -> l > r 退出循环条件，并且l 并没有超出右边界
这时候nums[l] == target, l就是左边界

#3.1 使用开区间寻找右边界   [1,   2,  3,  4,  4,  4,  4,  5]  target = 4
target  l   r   mid     action
4       0   8   4       target = nums[mid] -> l = mid +1 = 5
4       5   8   6       target = nums[mid] -> l = mid + 1 = 7  
4       7   8   7       target < nums[mid] -> r = mid = 7  -> l == r 循环条件推出
这时候返回值应该是l-1 = 6, 为右边界 

#3.2 使用闭区间寻找右边界   [1,   2,  3,  4,  4,  4,  4,  5]  target = 4
target  l   r   mid     action
4       0   7   3       target == nums[mid] -> l = mid + 1
4       4   7   5       target == nums[mid] -> l = mid + 1
4       6   7   6       target == nums[mid] -> l = mid + 1
4       7   7   7       target < nums[mid]  -> r = mid - 1 -> 6 ,这时候l > r退出循环条件，
这时候r并没有小于数组的左边界(0)，并且nums[r] == target, r 就是要找的右边界 6

#另外，可以直接使用bisect模块进行二分查找，
#接口: bisect.bisect_left(a, n),在有序数组a中要插入n,如果已经存在n返回其左边位置, 
#接口：bisect.bisect, bisect.bisect_right(a, n, lo = 0, hi = len(a)),在有序数组a中插入n,如果已经存在n,返回右边位置
#接口：bisect.insortleft(a, n, lo = 0, hi = len(a)), 在有序数组a中插入n





