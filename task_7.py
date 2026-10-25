def digit_root(num):

    num_str = str(num)

    while len(num_str) != 1:
        amount = 0
        for i in num_str:
            amount += int(str(i))

        num_str = str(amount)

    return int(num_str)

print(digit_root(889987))
