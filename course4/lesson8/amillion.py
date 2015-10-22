#!/usr/bin/env python3
import random
import timeit
"""
Comparison of a list() and comprehension applied to a list and a generator
"""


lst = [random.random() for x in range(1000000)]
print("list() applied to list:",
      timeit.timeit("list(lst)",
      "from __main__ import lst",
      number=10))
print("Comprehension applied to list:",
      timeit.timeit("[x for x in lst]",
      "from __main__ import lst",
      number=10))

gen = (random.random() for x in range(1000000))
print("list() applied to generator:",
      timeit.timeit("list(gen)",
      "from __main__ import gen",
      number=10))
print("Comprehension applied to generator:",
       timeit.timeit("[x for x in gen]",
       "from __main__ import gen",
       number=10))
