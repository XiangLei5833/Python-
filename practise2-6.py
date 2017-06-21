#!/usr/bin/env python

try:
    a = int(raw_input("Enter a number: "))
    if a > 0:
        print "The number is +"
    elif a < 0:
        print "The number is -"
    elif a == 0:
        print "The number is 0"
except ValueError:
    print "Please input again"
