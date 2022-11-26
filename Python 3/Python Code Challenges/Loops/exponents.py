def exponents(bases, powers):
    new_list = []
    for base in bases:
        for power in powers:
            new_list.append(base ** power)
    return new_list

print(exponents([2, 3, 4], [1, 2, 3]))