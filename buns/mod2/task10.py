def last_letters(str):
    ans = ""
    for i in range(len(str)):
        if str[i] == " ":
            ans += str[i-1]
    ans += str[-1]
    return ans


str = input()
print(last_letters(str))
