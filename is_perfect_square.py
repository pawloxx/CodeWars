"""
is_square (-1) # => false
is_square   0 # => true
is_square   3 # => false
is_square   4 # => true
is_square  25 # => true
is_square  26 # => false
"""
from math import sqrt

def is_square(n):
    return int(n) > -1 and sqrt(n) % 1 == 0


print(is_square(1905835656))