#!/usr/bin/env python

import sys
with open(sys.argv[1]) as file:
    for line in file:
	splits = line.rstrip()
	splits = splits.split("http://")[1]
	print(splits)