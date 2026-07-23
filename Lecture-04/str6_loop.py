rows = int(input("How many rows? "))
cols = int(input("How many columns? " ))

for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()
    