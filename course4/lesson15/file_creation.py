#!/usr/bin/env python3
import mmap
import sys
import os
from timeit import Timer


def create_empty_file(file_name, file_size):
    """
    Creates and empty file file_name, after trying to delete the file if it
    already exists.
    """
    try:
        os.remove(file_name)
    except FileNotFoundError:
        pass
    with open(file_name, "wb") as f:
        f.seek(file_size - 1)
        f.write(b'\0')
        f.flush()
    return file_name


def generate_chunks(file_size):
    """
    A generator to return a chunk_size and number of chunks per iteration.
    """
    chunk_size = 1
    while file_size % chunk_size == 0:
        number_of_chunks = int(file_size / chunk_size)
        yield (chunk_size, number_of_chunks)
        chunk_size = chunk_size * 2


def write_memory_mapped(chunk_size, number_of_chunks, mapf):
    offset = 0
    for chunk in range(number_of_chunks):
        mapf[offset:offset+chunk_size] = chunk_size * b'\0'
        offset = offset+chunk_size


def write_file(chunk_size, number_of_chunks, f):
    for chunk in range(number_of_chunks):
        f.write(chunk_size * b'\0')

if __name__ == "__main__":
    file_name = "/tmp/mmap.txt"
    file_size = 1024 * 1024 * 10
    create_empty_file(file_name, file_size)
    chunks = generate_chunks(file_size)

    with open(file_name, "r+b") as f:
        mapf = mmap.mmap(f.fileno(), file_size, access=mmap.ACCESS_WRITE)
        for chunk_size, number_of_chunks in chunks:
            mmap_write = Timer(
                "write_memory_mapped(chunk_size, number_of_chunks, mapf)",
                "from __main__ import "
                "write_memory_mapped, chunk_size, number_of_chunks, mapf")
            file_write = Timer(
                "write_file(chunk_size, number_of_chunks, f)",
                "from __main__ import "
                "write_file, chunk_size, number_of_chunks, f")
            print(79 * "-")
            print("chunk_size:", chunk_size, "bytes")
            print("number_of_chunks:", number_of_chunks)
            print("mmap_write:", mmap_write.timeit(1), "seconds")
            print("file_write:", file_write.timeit(1), "seconds")
