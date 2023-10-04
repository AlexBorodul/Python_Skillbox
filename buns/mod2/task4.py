def bin(n):
    s = ""
    while n > 0:
        s = str(n % 2) + s
        n = n // 2
    return s

def oct(n):
    s = ""
    while n > 0:
        s = str(n % 8) + s
        n = n // 8
    return s

def hex(n):
    s = ""
    a = "0123456789ABCDEF"
    while n > 0:
        s = str(n % 16) + s
        n = n // 16
    return s


num = int(input())
print(bin(num), oct(num), hex(num))