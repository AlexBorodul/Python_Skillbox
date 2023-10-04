def alphabet(str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    str = str.replace(", ", "")
    ans = ""
    numb = int(str[1::])
    for i in range(len(alphabet)):
        if alphabet[i] == str[0]:
            ans = alphabet[i + numb % 26]
    return ans


str = input()
print(alphabet(str))
a = -1000
