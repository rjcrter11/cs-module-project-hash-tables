# Your code here
import math
import random

# Build a lookup table
# Build off the first instance of v
# If its not in the table, copy slow function
# if it already is, return the lookup table


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


lookup_table = {}


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    v = math.pow(x, y)
    if v not in lookup_table:
        lookup_table[v] = math.factorial(v)
        lookup_table[v] //= (x + y)
        lookup_table[v] %= 982451653
        return lookup_table[v]
    return lookup_table[v]


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
