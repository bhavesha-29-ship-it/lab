def insert_in_sorted(x, l):
    r = []
    f = 0

    for i in l:
        if f == 0 and x < i:
            r.append(x)
            f = 1
        r.append(i)

    if f == 0:
        r.append(x)

    return r


print(insert_in_sorted(4, [1, 3, 9]))
print(insert_in_sorted(10, [1, 3, 9]))