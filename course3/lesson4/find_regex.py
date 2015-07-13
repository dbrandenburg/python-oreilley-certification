#!/usr/bin/env python3
import re

def position_search():
    sample_text = 'In the 1950s, mathematician Stephen Cole Kleene described automata theory and formal language theory in a set of models using a notation called "regular sets" as a method to do pattern matching. Active usage of this system, called Regular Expressions, started in the 1960s and continued under such pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry Spencer.'
    m = re.search('Regular Expressions', sample_text)
    return m.start(), m.end()