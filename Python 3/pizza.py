# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2,6,1,3,2,7,2]

num_two_dollar_slices = prices.count(2)

num_pizzas = len(toppings)

print(f'We sell {num_pizzas} different kinds of pizza!')

pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

print(pizza_and_prices)

pizza_and_prices = sorted(pizza_and_prices)
print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0][1]
print(cheapest_pizza)

priciest_pizza = pizza_and_prices[-1][1]
print(priciest_pizza)

pizza_and_prices.pop()
print(pizza_and_prices)

pizza_and_prices.insert(3, [2.5, "peppers"])
print(pizza_and_prices)

three_cheapest = list(pizza_and_prices[0:3])
print(three_cheapest)