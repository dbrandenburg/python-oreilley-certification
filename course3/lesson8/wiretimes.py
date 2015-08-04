#!/usr/bin/env python3
import struct

file = open("wireshark.bin", "rb")
file.read(24)
counter = 0
while True:
    packet_header = file.read(16)
    if not packet_header:
        break
    ts_sec, ts_usec, incl_len, orig_len = struct.unpack('=4i', packet_header)
    counter += 1
    print('packet number: ', counter, 'seconds:',
        ts_sec, ' microseconds: ', ts_usec)
    file.read(incl_len)

file.close()