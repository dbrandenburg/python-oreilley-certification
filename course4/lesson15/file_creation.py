#!/usr/bin/env python3
import mmap
import sys
import os

file_name = "/tmp/mmap.txt"
file_size = 1024 * 1024 * 10

try:
    os.remove(file_name)
except:
    pass

with open(file_name, "wb") as f:
    f.seek(file_size - 1)
    f.write(b'\0')
    sys.stdout.flush()

with open(file_name, "r+b") as f:
    mapf = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
