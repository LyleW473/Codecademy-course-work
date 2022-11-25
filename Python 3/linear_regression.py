"""
This is the work on Reggie_Linear_Regression_Skeleton.jpynb.
"""

# Part 1 
def get_y(m, b, x):
    y = m*x + b
    return y

print(get_y(1,0,7) == 7)
print(get_y(5,10,3) == 25)

def calculate_error(m, b, point):
    x_point = point[0] 
    y_point = point[1]
    difference = get_y(m, b, x_point) - y_point

    return abs(difference)

print(calculate_error(1, 0, (3,3)))
print(calculate_error(1, 0, (3, 4)))
print(calculate_error(1, -1, (3, 3)))
print(calculate_error(-1, 1, (3, 3)))


def calculate_all_error(m, b, points):
    total = 0
    for point in points:
        total += calculate_error(m, b, point)

    return total
    
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))

datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))

datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))

datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))

# Part 2

possible_ms = [m * 0.1 for m in range(-100,101)]
print(possible_ms)

possible_bs = [b * 0.1 for b in range(-200, 201)]


datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
smallest_error = float("inf") 
best_m = 0
best_b = 0

for m in possible_ms:
    for b in possible_bs:
        error = calculate_all_error(m, b, datapoints)
        if error < smallest_error:
            best_m = m
            best_b = b
            smallest_error = error

print(best_m, best_b, smallest_error)


# Part 3:
print(get_y(0.3, 1.7, 6))

