n = 5

for i in range(1, n + 1):
    # Print spaces
    for j in range(0, n - i):
        print(" ", end="")

    # Print increasing numbers
    for k in range(1, i + 1):
        print(k, end="")

    # Print decreasing numbers
    for m in range(i - 1, 0, -1):
        print(m, end="")

    print()
