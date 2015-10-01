"""
Program for optimization. Python 4, Lesson 5.

Calculates the groffle speed of a knurl widget
of average density given by user input.
"""

from math import log
from timeit import Timer

def groffle_slow(mass, density):
    total = 0.0
    for i in range(10000):
        masslog = log(mass * density)
        total += masslog/(i+1)
    return total

def groffle_fast(mass, density):
    def groffle_fast_inner(mass, density):
        masslog = log(mass * density)
        for i in range(10000):
            yield masslog/(i+1)
    return sum(groffle_fast_inner(mass, density))

def groffle_also_fast(mass, density):
        masslog = log(mass * density)
        return sum(masslog/(i+1) for i in range(10000))

mass = 2.5
density = 12.0

slow = groffle_slow(mass, density)
fast = groffle_fast(mass, density)
also_fast = groffle_also_fast(mass, density)

if slow == fast == also_fast:
    print("Restults are identical")
else:
    print("Results differ")


slow_timer = Timer("total = groffle_slow(mass, density)",
 "from __main__ import groffle_slow, mass, density")
slow_time = slow_timer.timeit(number=1000)
print("slow_time:", slow_time)

fast_timer = Timer("total = groffle_fast(mass, density)",
 "from __main__ import groffle_fast, mass, density")
fast_time = fast_timer.timeit(number=1000)
print("fast_time:", fast_time)

also_fast_timer = Timer("total = groffle_also_fast(mass, density)",
 "from __main__ import groffle_also_fast, mass, density")
also_fast_time = also_fast_timer.timeit(number=1000)
print("also_fast_time:", also_fast_time)
