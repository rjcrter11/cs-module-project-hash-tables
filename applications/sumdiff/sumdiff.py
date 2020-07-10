"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# Make dictionaries for adding and subtracting
# Nested loop through q numbers
# q[i] + q[j] in add dict
# q[i] - q[j] in subtract dict
# Nested loop through the dictionaries
# Conditional for  the two being equal

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

add_cache = {}
subtract_cache = {}


def f(x):
    return x * 4 + 6


def sum_diff(tuple):

    for i in range(len(q)):
        for j in range(len(q)):
            add_cache[(q[i], q[j])] = f(q[i]) + f(q[j])
            subtract_cache[(q[i], q[j])] = f(q[i]) - f(q[j])

    for x in add_cache:
        for y in subtract_cache:
            if add_cache[x] == subtract_cache[y]:
                calculation = f'f({x[0]}) + f({x[1]}) = f({y[0]}) - f({y[1]})'
                result = f"{f(x[0])} + {f(x[1])} = {f(y[0])} - {f(y[1])}"
                print(f'{calculation}  {result}')


sum_diff(q)
