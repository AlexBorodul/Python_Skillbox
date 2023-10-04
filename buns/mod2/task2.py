def square(num):
    per = 4 * num
    sq = num ** 2
    diag = num * 2 ** 0.5
    return "{0:5.2f} {1:5.2f} {2:5.2f}".format(per, sq, diag)


num = int(input())
print(square(num))
