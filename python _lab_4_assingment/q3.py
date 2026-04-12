def is_happy(n):
    s = set()

    while n != 1 and n not in s:
        s.add(n)
        t = 0

        while n > 0:
            d = n % 10
            t = t + d * d
            n = n // 10

        n = t

    return n == 1


print(is_happy(13))
print(is_happy(12))