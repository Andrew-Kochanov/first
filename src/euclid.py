def gcd(a, b):
    
    while a != b:
        a, b = max(a, b), min(a, b)
        a -= b
    return (a, b)


print(gcd(81, 27))