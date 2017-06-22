#!/usr/bin/env python

import os
ls = os.linesep

def Write():
    while True:
        fname = raw_input("Enter filename: ")
        if os.path.exists(fname):
            print "Error: '%s' already exsits" % fname
        else:
            break
    all = []
    print "\nEnter lines ('.' by itself to quit).\n"
    
    while True:
        entry = raw_input('> ')
        if entry == '.':
            break
        else:
            all.append(entry)
    fobj = open(fname, 'r')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()
    print Done


def Read():
    fname = raw_input('Enter filename: ')
    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print '*** file open error:', e
    else:
        for eachLine in fobj:
            print eachLine.strip()
        fobj.close()



if __name__ == '__main__':
    while True:
        print '''Please choose:
                 (1).file write
                 (2).file read
                 (3).quit
              '''
        choosenumber = raw_input("Enter a number: ")
        if choosenumber == 1:
            Write()
        elif choosenumber == 2:
            Read()
        elif choosenumber == 3:
            break
        else:
            print 'Done'
