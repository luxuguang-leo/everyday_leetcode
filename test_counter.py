#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import collections

c = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
print(c)

for ch in 'abcdef':
    print("char times", ch, c[ch])

print(c.most_common(2))
for ch, cnt in c.elements():
    print(ch, cnt)
