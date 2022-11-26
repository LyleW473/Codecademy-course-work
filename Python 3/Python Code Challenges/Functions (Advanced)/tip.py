def tip(total, percentage):
    tip_amount = total * (percentage / 100)
    return tip_amount

print(tip(10, 25))
print(tip(0, 100))