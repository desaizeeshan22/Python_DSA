def binary_to_decimal(binary_string):
    res = 0
    base = 1
    for i in range(len(binary_string) - 1, -1, -1):
        num_added = binary_string[i] == "1"
        res += (base * num_added)
        base *= 2
    return res


print(binary_to_decimal("1101"))
