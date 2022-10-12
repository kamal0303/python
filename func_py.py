def disccalc(cp, discount):
    discount = cp * (discount/100)
    selling_price = cp - discount
    return selling_price


sp = disccalc(660, 30)
print(sp)
