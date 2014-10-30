#!/usr/bin/python

'''
Implementation of tree like tool in linux environment without recursion.

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

def graph(dest_dir):
    priv_path = ''
    dir_state = {}
    state_flag = []
    if dest_dir[-1] == '/':
       dest_dir = dest_dir[:-1]

    orig = len(dest_dir.split('/'))
    dir_state[dest_dir[:dest_dir.rfind('/')]]=' '

    for dirpath, dirnames, filenames in os.walk(dest_dir):
        dir_state[dirpath]=dirnames

    for dirpath, dirnames, filenames in os.walk(dest_dir):
        bar_space = '|   '
        space ='    '
        space_bar = '  '
        arr = '`-- '

        if dirpath == dest_dir:
            print '.'
            continue

        priv = dirpath[:dirpath.rfind('/')]

        if state_flag:
            for flag in state_flag:
                if (len(dirpath.split('/')) - orig) <= flag:
                    state_flag.remove(flag)

        if (dirpath == priv+'/'+dir_state[priv][-1]):
            state_flag.append(len(dirpath.split('/')) - orig-1)

        for i in range((len(dirpath.split('/')) - orig)-1):

            if i in state_flag:
                space_bar = space_bar+space
            else:
                space_bar = space_bar+bar_space

        if (len(dirpath.split('/')))==orig:
            print space+arr+ dirpath.split('/')[-1]
        else:
            print space_bar+arr+dirpath.split('/')[-1]

        for name in filenames:
            if (len(dirpath.split('/'))==orig) :
                print space+arr+name
            else:
                if (dirpath == priv+'/'+dir_state[priv][-1]):
                    print space_bar+space+arr+name
                else:
                    print space_bar+bar_space+arr+name

        priv_path = dirpath

arg = sys.argv[1]
graph(arg)
