#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from random import randrange

seq = [randrange(10**10) for i in range(100)]
dd = float('inf')
ret = []

#O(N^2)
'''
for x in seq:
    for y in seq:
        if x == y:
            continue
        d = abs(x-y)
        if d < dd:
            ret.append((x, y))
            dd = d

print ret[-1]
'''

#O(NlogN)
seq.sort()
for x in range(len(seq)-1):
    d = abs(seq[x] - seq[x+1])
    if d < dd:
        dd = d
        ret.append((seq[x], seq[x+1]))
print ret[-1]
    


