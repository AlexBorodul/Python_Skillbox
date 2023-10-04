def eq(str):
    count = 0
    for i in range(len(str)):
        if str[i] == '0': count += 1
        elif str[i] == '1': count -= 1
    if count == 0: return 'yes'
    return 'no'


string = input()
print(eq(string))
