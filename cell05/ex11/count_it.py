#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
else:
    count = len(sys.argv) - 1
    print(f"parameters: {count}")
    
    for param in sys.argv[1:]:
        print(f"{param}: {len(param)}")
