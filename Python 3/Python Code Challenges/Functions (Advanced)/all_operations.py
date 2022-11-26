def lots_of_math(a,b,c,d):
    result1 = a + b
    print(result1)
    result2 = c - d
    print(result2)
    result3 = result1 * result2
    print(result3)
    
    return result3 % a

print(lots_of_math(1, 2, 3, 4))
print(lots_of_math(1, 1, 1, 1))