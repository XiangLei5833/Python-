#!/usr/bin/env python
# -*- coding:utf-8 -*-

class C:
    def __nonzero__(self):
        return False

c = C()    # 类实例
bool(c)
bool(C)    # 表示确定这个类是否存在
