#!/usr/bin/env python3


class ctx:
    def __init__(self, raising=True):
        self.raising = raising

    def __enter__(self):
        dummyobj = object()
        return dummyobj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ValueError:
            print("Gracefully supressing ValueError")
            return self.raising
        elif self.raising:
            return not self.raising

with ctx() as c:
    int("Cause ValueError.")
