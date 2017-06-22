#!/usr/bin/env python

'read add display text file'

# get filename
fname = raw_input("Enter filename: ")
print

# attemp to open and reading
try:
    fobj = open(fname, 'r')
except IOError, e:
    print '*** file open error:', e
else:
    for eachLine in fobj:
        print eachLine
    fobj.close()
