def print_all(*aegs):
    for index, arg in enumerate(aegs):
        print(f"Argument {index + 1}: {arg}")

print_all("Python", 3.8, True, [1, 2, 3], {"key": "valre"})
