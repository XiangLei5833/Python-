#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 计算面积和体积

from math import pi


def square(length):
    area = length ** 2
    return 'The area of square %d' % area

def cube(length):
    volume = length ** 3
    return 'The volumn of cube %d' % volumn

def circle(radius):
    area = pi * redius**2
    return 'The area of square %d' % area

def globe(radius):
    volumn = (4/3)*pi*radius**3
    return 'The volumn of globe %d' % volumn



if __name__ == '__main__':
    try:
        num = float("Enter a number: ")
        print square(num)
        print cube(num)
        print circle(num)
        print globe(num)
    except ValueError:
        print 'input error'
