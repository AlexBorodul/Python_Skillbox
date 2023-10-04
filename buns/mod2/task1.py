def ostatok(string):
    string = string.replace(', ', ',')
    n = 0
    for i in range(len(string)):
        if string[i] == ",":
            n = i
    a = int(string[:n])
    b = int(string[n+1::])
    return a % b


string = input()
print(ostatok(string))
