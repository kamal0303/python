mrp = int(input("Enter mrp of product "))
discount = int(input("Enter discount percentage "))
calculation = mrp * (discount/100)
sp = mrp - calculation
print(sp)
