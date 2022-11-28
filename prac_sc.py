# l = ["kamal", 10.2, 1988]
# for s in l:
#     print(s)

# counter variable
# while (test expression)
# statement
# increment / decrement

# counter = 1
# while counter <= 4:
#     print('a')
#     counter = counter + 1

# x = 10
# y = 10.0
# if x == 10:
#     print("x is equal to 10")
# if x > 5:
#     print("x is greate than 5")
# if x == y:
#     print("x is equal to y")

# a = [1, 2, 3, 4, 5, "kamal"]
# i = 0
# while (i < len(a)):
#     print(a[i])
#     i += 1

# a = [1, 2, 3, 4, 5, "kamal"]
# i = 0
# for i in a:
#     print(i)
# i += 1

# n = int(input("Enter any number: "))
# i = 1
# while (i <= n):
#     if (n % i == 0):
#         print(i)
#     i += 1

# li = ['A']
# li.extend('BCD')
# print(li)

# n = int(input("enter any number: "))
# i = 1
# while (i <= n):
#     if n % i == 0:
#         print(i)
#         i = i + 1


# s = "Radar"
# print(s.strip('rarely'))

# a = 5
# for i in range(10):
#     print(f"{a}X{i+1}= {a * (i+1)}")

def Greet(item):
    print("Good morning")


l1 = ["harry", "soham", "kamal", "shrey"]
for item in l1:
    if item.startswith("s"):
        print(f"Greet{item}")
