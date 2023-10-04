def begin(str):
    let = str[-1]
    count = 0
    for i in range(0, len(str)):
        if str[i] == let:
            count += 1
        else:
            break
    return count


string = input()
print(begin(string))