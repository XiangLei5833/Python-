#!/usr/bin/env python
# -*- coding: utf-8
# 时间转换

def Min(a, b):
    min = a*60 + b
    return min


if __name__ == '__main__':
    M = input('Enter a time: ')
    try:
        (h, m) = M.split(':')
        print Min(h, m)
    except ValueError:
        print 'Please input again'

