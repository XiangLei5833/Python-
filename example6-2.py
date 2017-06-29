#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 切片索引到更多内容（负数索引）

s = 'abcde'
for i in [None] + range(-1, -len(s), -1):    # 此处－1用于将range()读取顺序反转，变为从右到左。None使的可以完全显示整个序列，在负数环境之下。
    print s[:i]


# 下面这个和上面输出结果相同
for i in range(5,0,-1):
    print s[:i]
