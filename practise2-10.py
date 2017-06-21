#!/usr/bin/env python

try:
    a = float(raw_input("Enter a number(0~100): "))
    if 0 < a < 100:
        print "succession"
    else:
        print 'ValueError,Please input again'
except:
    print "Please input again"
