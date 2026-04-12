def reduce(n, d):
    a = n
    b = d

    while b != 0:
        a, b = b, a % b

    return (n // a, d // a)


print(reduce(10, 50))
print(reduce(1, 2))