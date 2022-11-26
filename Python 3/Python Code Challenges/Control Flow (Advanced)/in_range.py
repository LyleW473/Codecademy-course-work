def in_range(num, lower, upper):
    if num >= lower and num <= upper:
        return True
    else:
        return False

print(in_range(20, 5, 11))