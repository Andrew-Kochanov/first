def gcd(a, b):
    while a != b:
        a, b = max(a, b), min(a, b)
        a -= b
    return (abs(a), abs(b))


print(gcd(81, 27))