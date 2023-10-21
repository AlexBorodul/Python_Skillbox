def degree(a, n):
    if n == 1:
        return a
    elif n % 2 == 0:
        return degree(a, n // 2) * degree(a, n // 2)
    else:
        return degree(a, n // 2) * degree(a, n // 2) * a

print(degree(int(input()), int(input())))
