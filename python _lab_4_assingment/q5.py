def perfect_square(l):
    r = []

    for i in l:
        x = int(i ** 0.5)
        if x * x == i:
            r.append(i)

    return r


print(perfect_square([1, 25, 39, 36, 45, 74]))