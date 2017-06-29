#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 原始字符串操作符

import re

m = re.search('\\[rtfvn]', r'Hello World!\n')
if m is not None: m.group()

m = re.search(r'\\[rtfvn]', r'Hello world!\n')
if m is not None: m.group()
