#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 字符串模板，格式化字符串替代品

from string import Template

s = Template('There are ${howmany} ${lang} Quotation Symbols')
print s.substitute(lang = 'Python', howmany = 3)

y = Template('we are at $')
print y.substitute(100)
