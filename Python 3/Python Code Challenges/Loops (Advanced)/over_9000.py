def over_nine_thousand(list):
    sum = 0
    for number in list:
        sum += number
        if sum > 9000:
            break
    return sum

print(over_nine_thousand([8000, 900, 120, 5000]))