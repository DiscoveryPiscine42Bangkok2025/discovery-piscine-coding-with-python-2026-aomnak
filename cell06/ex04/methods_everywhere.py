#!/usr/bin/env python3

import sys

def shrink(s):
    print(s[:8])

def enlarge(s):
    while len(s) < 8:
        s += "Z"
    print(s)

if len(sys.argv) == 1:
    print("none")
else:
    for param in sys.argv[1:]:
        if len(param) > 8:
            shrink(param)
        elif len(param) < 8:
            enlarge(param)
        else:
            print(param)
