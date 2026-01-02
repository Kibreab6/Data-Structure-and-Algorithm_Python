def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


print_items(10)


# time complexity: O(n) - the two loops are both O(n) and add up to O(2n)
# in this case we drop the constant and the time complexity simplifies to O(n)
