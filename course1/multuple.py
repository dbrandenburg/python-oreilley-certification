#!/usr/local/bin/python3

pairs = ((1, 1), (2, 2), (12, 13), (4, 4), (99, 98))

for factors in pairs:
    product = factors[0]*factors[1]
    fmt = "{0:>4} = {1:>2} x {2:>2}"
    print(fmt.format(product,factors[0],factors[1]))