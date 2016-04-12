# filter
def isMultipleOf5Or3(x):
    return x % 3 == 0 or x % 5 == 0

print filter(isMultipleOf5Or3, range(1, 25))

# map
def square(x):
    return x * x

print(map(square, [2, 14, 19]))

def add(x, y):
    return x + y

# multiple sequences are allowed
# number of sequences should be equal to number of parameters of the mapping function
print(map(add, [1, 2, 3], [4, 5, 6]))

# reduce
print(reduce(add, [1, 2, 3], 0))


