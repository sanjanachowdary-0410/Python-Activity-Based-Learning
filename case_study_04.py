n = 4  # Half-height (rows from top to widest row)

if n < 2:
    print("Invalid dimension: please use an integer >= 2 for a hollow diamond.")
else:
    # Upper half including middle row
    for r in range(1, n + 1):
        outer_pad = "  " * (n - r)
        if r == 1:
            print(f"{outer_pad}1")
        else:
            inner_pad = "  " * (2 * r - 3)
            print(f"{outer_pad}{r}{inner_pad}{r}")

    # Lower half
    for r in range(n - 1, 0, -1):
        outer_pad = "  " * (n - r)
        if r == 1:
            print(f"{outer_pad}1")
        else:
            inner_pad = "  " * (2 * r - 3)
            print(f"{outer_pad}{r}{inner_pad}{r}")
