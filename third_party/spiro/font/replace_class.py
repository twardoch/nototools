#!/usr/bin/env python


import sys

srfile = open(sys.argv[1])
table = {}
for line in srfile.readlines():
    clas, repl = line.split()
    if repl[-1] not in "-?":
        table["class" + clas] = repl

for line in sys.stdin.readlines():
    fn, clas = line.split()
    if clas in table:
        print(fn, table[clas])
