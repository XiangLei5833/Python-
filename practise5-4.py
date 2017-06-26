#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 计算闰年

def Leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False    # 能被400整除
        else:
            return True    # 能被4整除不能被100整除
    else:
        return False
            


if __name__ == '__main__':
    year = int(input('Enter a year: '))
    Ly = Leap_year(year)
    print Ly
