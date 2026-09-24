def apply_twice(func, value):
    return func(func(value))

def increment(x):
    return x + 1

result = apply_twice(increment, 5)
print(result)  # Output: 7