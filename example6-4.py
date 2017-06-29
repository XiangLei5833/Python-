#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 标识符检查

import string

alphas = string.letters + '_'
nums = string.digits
print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long'

myInput = input("Enter a Identifier: ")
if len(myInput) > 1:
    if myInput[0] not in alphas:
        print False
    else:
        for otherchar in myInput[1:]:
            if otherchar not in alphas+nums:
                print False
                break
        print 'OK'
else:
    print 'Please input again'
