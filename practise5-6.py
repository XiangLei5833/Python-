#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 计算机程序

ope = ['+', '-', '*', '/','%', '**']
exp = input("Enter a expression: ")

def complete():
    try:
        for op in ope:
            cmp = exp.split(op)
            m = cmp[0]
            n = cmp[1]
            if op == '+':
                return sum(m,n)
            if op == '-':
                return m - n
            if op == '*':
                return m * n
            if op == '/':
                return m / n
            if op == '%':
                return m % n
            if op == '**':
                return pow(m, n)
    except ValueError:
        print 'Pleae input again'


if __name__ == "__main__": 
    Complete = complete()
    print Complete
