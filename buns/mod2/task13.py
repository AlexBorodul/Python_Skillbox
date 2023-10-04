def strix(num):
    sum1 = 0
    sum2 = 0
    for i in range(0, len(num)):
        if i % 2 == 0:
            sum1 += int(num[i])
        else:
            sum2 += int(num[i])
    if (sum2 * 3 + sum1) % 10 == 0:
        return "yes"
    return "no"


str = input()
print(strix(str))
