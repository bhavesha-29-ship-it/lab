def get_range(*a):
    mn = a[0]
    mx = a[0]

    for i in a:
        if i < mn:
            mn = i
        if i > mx:
            mx = i

    return mx - mn


print(get_range(1.0, 2.9, 3.0, 4.5, 5.0))