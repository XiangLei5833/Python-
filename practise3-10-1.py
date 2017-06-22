#!/usr/bin/env python

fname = raw_input("Enter filename: ")

if os.path.exists(fname):
    fobj = open(fname, 'r')
    for eachLine in fobj:
        print eachLine
    fobj.close()
else:
    print "*** file open error: don't find fname file"
