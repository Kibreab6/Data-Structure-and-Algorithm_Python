def print_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)


print_items(1, 10)
# time complexity: O(a + b) - scales linearly with the sum of two inputs
# in this case, we cannot simplify the time complexity further since we are using two different parameters
