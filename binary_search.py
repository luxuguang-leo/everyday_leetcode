#patton 1, standard
#搜索区间是[left, right], while l <= r 的中止条件是left = Right + 1,区间就是[Right +1 , Right]
#右区因为已经判断过了nums[mid]元素，所以需要再除掉mid元素的 [left, mid-1] 或者 [mid + 1, right]来搜索

def binaySearch(nums, target):
    if not nums:
        return -1
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (r-l)//2 + l
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            r = mid -1
        elif target > nums[mid]:
            l = mid +1
    return -1

#patten 2
#这个算法用来求区间左边界，也就是第一个出现target的左边界
def binarySearchLeftBoundary(nums, target):
    if not nums:
        return -1
    l, r = 0 , len(nums)
    while l < r:
        mid = (r-l)//2 + l
        if target == nums[mid]:
            right = mid
        elif target < nums[mid]:
            r = mid
        elif target > nums[mid]:
            l = mid + 1
    if left == len(nums):
        return -1
    if nums[left] == target:
        return left
    else:
        return -1

#patten 3
#寻找区间右边界，也就是出现target的最后一个值，也就是右边界

def binarySearchRightBoundary(nums, target):
    if not nums:
        return -1
    l, r = 0, len(nums)
    while l < r:
        if target = nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            r = mid
        elif target > nums[mid]:
            l = mid +1
    return left -1




