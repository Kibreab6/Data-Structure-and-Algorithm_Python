num1 = 11

num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

num2 = 22

print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))


# in the above example, num1 and num2 intially points to the same memory location
# when we update num2 to 22, it now points to a different location and illustartes that
# integers are immutable in python


dict1 = {
    'value': 11
}

dict2 = dict1

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict2['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
# this example illustrates that both dict1 and dict2 points to the same memory location
# when the value is updated via dict_2, it also reflects in dict1 since dictionaries are mutable
