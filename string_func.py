# string1 = "datascientist"
# # string1.casefold()
# print(string1.count('a'))
# print(string1.center())

# string to integer
A = "50"
print(f"Data type before: {type(A)}")
A = int(A)
print(f"Data Type After: {type(A)}")

# float to integer
A = 50.22
print(f"Data type before: {type(A)}, value of A: {A}")
A = str(A)
print(f"Data type after: {type(A)}, value of A: {A}")

# integer to float
A = 50
print(f"Data type before: {type(A)}, value of A: {A}")
A = float(A)
print(f"Data type after: {type(A)}, value of A: {A}")

# integer to boolean
A = -0
print(f"Data type before: {type(A)}, value of A: {A}")
A = bool(A)
print(f"Data type after: {type(A)}, value of A: {A}")
