#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Unicode字符串编码解码例子

CODEC = 'utf-8'
File = 'unicode.txt'

hello_out = u'Hello world\n'
bytes_out = hello_out.encode(CODEC)
f = open(File, 'w')
f.write(bytes_out)
f.close()

f = open(File)
byte_in = f.read()
f.close()
hello_in = byte_in.decode(CODEC)
print hello_in,
