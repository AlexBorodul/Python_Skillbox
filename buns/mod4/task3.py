def eucklid(a, b):
    if b == 0:
        return a
    return eucklid(b, a % b)

print(eucklid(int(input()), int(input())))