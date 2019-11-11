#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import heapq

#show usage of heapq in Python, in Python, it's implemented
#in min heap tree

list_nums = [21, 67, 33, 13, 40, 89, 71, 19]
largest_nums = heapq.nlargest(2, list_nums)
print("Test nlargest:")
print("the 2 largest elem:", largest_nums)

#heappush(), insert one elements
heapq.heappush(list_nums, 100)
largest_nums = heapq.nlargest(2, list_nums)
print("Test heappush:")
print("After insertion 2 largest elem:", largest_nums)
print(list_nums)

list_nums1 = [x for x in range(10,0,-1)]
print("Init list:", list_nums1)
heap_list = []
for n in list_nums1:
    heapq.heappush(heap_list, n)
print("Heap afterthen:", heap_list)

#heappop()
print("Test heapop:")
heapq.heappop(heap_list)
print("Heap after heappop:", heap_list)

#heappushpop() = heappush+heappop
print("Test heappushpop:" )
heapq.heappushpop(heap_list, 11)
print("Heap after heappushpop:", heap_list)

#heapify, this func accepts an arbitrary list and convert it to a heap

list_nums2 = [_ for _ in range(10,-1,-1)]
print("Test heapify:", list_nums2)
heapq.heapify(list_nums2)
print("heap after heapify:", list_nums2)

#heapreplace, delete the smallest elem from the heap and insert a new item heapreplace = heappop+heappush

heapq.heapreplace(list_nums2, -2)
print("heap after heapreplace:", list_nums2)

#nlargest, find the n largest elem from a given iterable, accepts a key which is a functions of one arguments

#heapq.nlargest(n, iterable, key=None)

print("heap with 3 larget elems:", heapq.nlargest(3,list_nums2))




'''
the time complexity of functions in heapq:
heapify(k) O(k)
heappush  O(log k)
heappop   O(log k)
nlargest/nsmallest O(log t)
'''
