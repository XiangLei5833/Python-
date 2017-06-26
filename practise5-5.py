#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 计算硬币数

def Coinnumber(coin):
    (N25, coin) = divmod(coin, 25)    # 也可以使用 for i in [25, 10, 5, 1]
    (N10, coin) = divmod(coin, 10)
    (N5, coin) = divmod(coin, 5)
    (N1, coin) = divmod(coin, 1)
    return '25 cent is %d, 10 cent is %d, 5 cent is %d, 1 cent is %d' % (N25, N10, N5, N1)    # 也可以使用 format[]


if __name__ == '__main__':
    coin = int(input("Enter a coin number: "))
    C = Coinnumber(coin) 
    print C
