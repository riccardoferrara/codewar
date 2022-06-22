# Build a pyramid-shaped tower given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ", 
#   "*****"
# ]


def tower_builder(n_floors):
    # build here
    return [ ((2*i)+1)*'*' for i in range(0, n_floors)]


print(tower_builder(3)) # ['  *  ', ' *** ', '*****']))