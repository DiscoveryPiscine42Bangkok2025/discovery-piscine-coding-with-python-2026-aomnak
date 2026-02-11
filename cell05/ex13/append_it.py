#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
else:
    found = False

    for param in sys.argv[1:]:
        if not param.endswith("ism"):
            print(param + "ism")
            found = True

    if not found:
        print("none")
