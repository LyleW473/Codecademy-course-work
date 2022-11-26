weight = 4.8
cost = 0

premium_ground_shipping = 125.00
ground_shipping = True

if ground_shipping == False:
    drone_shipping = True
elif ground_shipping == True:
    drone_shipping = False

# Ground shipping
if ground_shipping == True:
    if weight <= 2:
        cost = (weight * 1.50) + 20.00
    elif 2 < weight <= 6:
        cost = (weight * 3.00) + 20.00
    elif 6 < weight <= 10:
        cost = (weight * 4.00) + 20.00
    elif weight > 10:
        cost = (weight * 4.75) + 20.00

else:
    # Drone shipping
    if weight <= 2:
        cost = (weight * 4.50)
    elif 2 < weight <= 6:
        cost = (weight * 9.00) 
    elif 6 < weight <= 10:
        cost = (weight * 12.00)
    elif weight > 10:
        cost = (weight * 14.25)

print(cost)
print(f'The premium ground shipping is {premium_ground_shipping}')


