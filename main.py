#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys


def main():
    size = int(sys.stdin.readline().strip())
    switches = [False] * size
    for line in sys.stdin:
        line = line.strip()
        start, end = line.split(" ")
        start, end = int(start), int(end)
        start, end = min(start, end), max(start, end)
        for i in xrange(start, end + 1):
            switches[i] = not switches[i]
    print(sum(switches))
    return 0


if __name__ == "__main__":
    sys.exit(main())
