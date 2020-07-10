# Your code here
# Plan
# Init a dictionary
# All params >= 0
# set base case
# params are keys in a tuple
# if keys aren't in cache, add them to it


cache = {}


def expensive_seq(x, y, z):
    keys = (x, y, z)
    if x <= 0:
        return y + z

    if keys not in cache:
        cache[keys] = expensive_seq(
            x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)

    return cache[keys]


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
