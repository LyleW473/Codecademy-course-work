def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    if budget < food_bill + electricity_bill + internet_bill + rent:
        return True
    else:
        return False


print(over_budget(100, 5, 5, 10, 20))
