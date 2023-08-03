#!/usr/bin/env python

import os
import sys

if len(sys.argv) < 2:
    exit(1)

path = sys.argv[1]

for p in os.listdir(path):
    if not os.path.exists(f'{path}/{p}'):
        print(p)
