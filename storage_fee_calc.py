x = float(input("Enter length: "))
y = float(input("Enter Width: "))
z = float(input("Enter Height: "))

total_weight = x * y * z
cubic_feet = total_weight/28316.84
storage_fee = cubic_feet * 33
print(f"storage fee per month is ", round(storage_fee,2))