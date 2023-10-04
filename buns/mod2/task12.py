def repl(str):
    str = str.replace('-', '')
    str = str.replace(')', '')
    str = str.replace('(', '')
    str = str.replace(' ', '')
    return str


string = input()
print(repl(string))
