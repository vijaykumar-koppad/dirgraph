#!/usr/bin/python
'''
Implementation of tree like tool in linux environment with recursion.

Output on any directory look like
.
  `-- x86
  |   `-- .built-in.o.cmd
  |   `-- include
  |   |   `-- asm
  |   |       `-- Kbuild
  |   |       `-- xen
  |   |       |   `-- events.h
  |   |       `-- uv
  |   |       |   `-- bios.h
  |   |       `-- visws
  |   |           `-- cobalt.h
  |   `-- crypto
  |   |   `-- .aes-i586-asm_32.o.cmd

'''

import os
import sys

def crawlr(dest_dir, state_flag, depth):
    dirnames = []
    filenames = []
    bar_space ='|   '
    space ='    '
    arr = '`-- '
    indent = '  '
    basename = os.path.basename(dest_dir)
    for name in os.listdir(dest_dir):
        fullpath = os.path.join(dest_dir, name)
        if os.path.isfile(fullpath):
            filenames.append(name)
        if os.path.isdir(fullpath):
            dirnames.append(name)

    for i in range(depth-1):
        if i in state_flag:
            indent = indent + space
        else:
            indent = indent + bar_space

    if not depth is 0:
        print indent + arr + basename

    if depth == 0:
        pacer = indent
    elif depth-1 in state_flag:
        pacer = indent + space
    else:
        pacer = indent + bar_space
    for name in filenames:
        print pacer + arr + name

    for dirname in dirnames:
        if dirname is dirnames[-1]:
            state_flag.add(depth)
        dirname = os.path.join(dest_dir, dirname)
        crawlr(dirname, state_flag, depth+1)
        if depth in state_flag:
            state_flag.remove(depth)

def graph(dest_dir):
    dirnames = []
    filenames = []
    state_flag = set()
    depth = 0
    print "."
    crawlr(dest_dir,state_flag,depth)

arg = sys.argv[1]
graph(arg)
