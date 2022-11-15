exp = -1
total = 0
maxexp = 0
minexp = 0


while exp != 0:
    exp = int(input("what is the expense? (type 0 to stop)"))
    total = total + exp
    if exp > maxexp:
        maxexp = exp
    # elif minexp <
    # minexp = min(exp)

    print("your total expenditure is " + str(total))
    print("the maximum you spend is " + str(maxexp))
    # print("the minimum you spend is " + str(minexp))
