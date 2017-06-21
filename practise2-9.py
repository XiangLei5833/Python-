#!/usr/bin/env python

a = []
sum = 0
for i in range(5):
    b = int(input("n%d = " % (i+1)))
    a.append(b)
    sum = sum + b
print 'aver = ',float(sum)/len(a)
