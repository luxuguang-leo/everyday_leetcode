#bubble sorting 

def bubbleSort(nums):
    cnt = len(nums)
    for i in range(cnt):
        for j in range(i+1, cnt):
            if nums[i] >nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

#insert sorting
def insertSort(nums):
    l = len(nums)
    for i in range(1, l):
        key = nums[i]
        j = i -1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

#selection sorting
def selectSort(nums):
    for i in range(0, len(nums)):
        min_ind = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_ind]:
                min_ind = j
        nums[i], nums[min_ind] = nums[min_ind], nums[i]
    return nums

'''
def shellSort(nums):
    l = len(nums)
    step = 2
    group = l/step
    while group > 0:
        for i in range(group):
            j = i + group#other elements in one group
            while j < l:
                k = j - group
                key = nums[j]
                while 

        group /= step
    return nums
'''

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result = result + left + right
    return result

def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)

def partation(nums, left, right):
    pivot = nums[left]
    start = left +1
    end = right
    while start < end:
        while start <= end and nums[start] < pivot:
            start += 1
        while start <= end and nums[end] > pivot:
            end -= 1
        if start <  end:
            nums[start], nums[end] = nums[end], nums[start]
    nums[left], nums[end] = nums[end], nums[left]
    return end


def quickSortHelper(nums, left, right):
    if left < right:
        partation_ind = partation(nums, left, right)
        quickSortHelper(nums, left, partation_ind-1)
        quickSortHelper(nums, partation_ind+1, right)
    return nums


def quickSort(nums):
    return quickSortHelper(nums, 0, len(nums)-1)


arr0 = [64, 34, 25, 12, 22, 11, 90] 
print ("before sorting:")
print (arr0)
print ("Bubble sorting")
print (bubbleSort(arr0))
arr1 = [64, 34, 25, 12, 22, 11, 90]
print ("Insert sorting")
print (insertSort(arr1))
arr2 = [64, 34, 25, 12, 22, 11, 90]
print ("select sorting")
print (selectSort(arr2))

arr3 = [64, 34, 25, 12, 22, 11, 32]
print ("merge sorting %d", arr3)
print (mergeSort(arr3))

arr4 = [64, 34, 25, 12, 22, 11, 32]
print ("quick sorting %d", arr4)
print (quickSort(arr4))