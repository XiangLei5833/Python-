#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 取余计算

def Even():
    even = []
    for i in range(21):
        if i % 2 == 0:
            return i
        even.append(i)
        return even

def Odd():
    odd = []
    for i in range(21):
        if i % 2 == 1:
            return i        
        odd.append(i)
        return odd

def Mod():
    m = float(input('Enter a number: '))
    n = float(input('Enter a number: '))
    if m % n == 0:
        print True
    if m % n != 0:
        print False

        
if __name__ == '__main__':
    e = Even()
    o = Odd()
    print e
    print o
    Mod()
