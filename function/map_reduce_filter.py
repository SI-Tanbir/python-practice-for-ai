import functools

total = functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])

# print(total)

doubled = list(map(lambda x: x * 2, [1, 2, 3, 4, 5]))

print(doubled)

names = ["ali", "reza", "mehdi", "sina", "sara"]

# Option 1: Using map() function
list(map(print, names))

# Option 2: If you just want to print each name, you can use a simple for loop
# for name in names:
#     print(name)
