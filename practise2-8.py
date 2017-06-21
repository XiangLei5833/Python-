#!/usr/bin/env python

a = [1,2,3,4,5]
i = 0
sum = 0
while i < len(a):
    sum = a[i]
    sum += sum
    i += 1
print sum



print "Enter five number"
b = []
i = 0
sum = 0
while i < 5:
    v = int(raw_input('n%d = ' % (i+1)))
    b.extend([v])
    sum = sum + b[i]
    i += 1
print b
print sum



print "Enter five number"
b = []
sum = 0
for i in range(5):
    v = int(input("n%d = "% (i+1)))
    b.extend([v])
    sum = sum + b[i]
print b
print sum
