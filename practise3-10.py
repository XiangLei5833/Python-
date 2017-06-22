#!/usr/bin/env python

import os
ls = os.linesep

fname = raw_input("Enter filename: ")

while True:
    try:
        fobj = open(fname, 'r')
    except IOError, e:
        all = []
        print "\nEnter lines ('.' by lines to quit).\n"
        while True:
            entry = raw_input('> ')
            if entry == '.':
                break
            else:
                all.append(entry)

        fobj = open(fname, 'w')
        fobj.writelines(["%s%s" % (x, ls) for x in all])
        fobj.close
        print 'Done'
    else:
        print "Error: '%s' already exists" % fname
    break
