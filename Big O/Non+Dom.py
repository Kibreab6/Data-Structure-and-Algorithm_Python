def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)


print_items(10)
# time complexity: O(n^2) - scales quadratically with the number of elememts
# The nested loops O(n^2) dominate the single loop O(n) - the single loop is non-dominant
