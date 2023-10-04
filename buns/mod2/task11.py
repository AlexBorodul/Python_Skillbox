def dubl(num):
    fl = False
    for i in range(0, len(num), 2):
        for j in range(i + 2, len(num), 2):
            if num[i] == num[j]:
                fl = True
                break
    return fl


str = input()
print(dubl(str))
