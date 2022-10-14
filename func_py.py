# def disccalc(cp, discount):
#     discount = cp * (discount/100)
#     selling_price = cp - discount
#     return selling_price


# sp = disccalc(660, 30)
# print(sp)

# pi = 22/7
# rounded_pi = round(pi, 2)
# print(rounded_pi)

def add_fourorfive(input):
    if input < 10:
        output = input + 4
    elif input >= 10:
        output = input + 5
    return output


output = add_fourorfive(10)
print(output)


def evaluate_temp(temp):
    message = "Normal temperature"
    if temp > 38:
        message = "Fever"
    return message


print(evaluate_temp(39))
