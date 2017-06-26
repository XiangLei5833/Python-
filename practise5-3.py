#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 计算成绩

def Achi(mark):
    if 90 <= mark <= 100:
        print 'A: the student of achievement'
    elif 80 <= mark < 90:
        print 'B: the student of achievement'
    elif 70 <= mark < 80:
        print 'C: the student of achievement'
    elif 60 <= mark <70:
        print 'D: the student of achievement'
    else:
        print 'F'


if __name__ == '__main__':
    mark = float(input("Enter student mark: "))
    Achi(mark)
