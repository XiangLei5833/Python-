#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 转换温度

def Tem(F):
    C = (F-32) * (5.0/9)    # 此处必须浮点数，要不结果为NONE
    print C


if __name__ == '__main__':
    try:
        F = float(input('Enter a number: '))
        T = Tem(F)
        print T 
    except ValueError:
        print 'Please input again'
