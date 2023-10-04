def domen(str):
    dot1 = str.find(".")
    dot2 = str.rfind(".")
    dom1 = str[dot2+1::]
    dom2 = str[dot1+1:dot2]
    dom3 = str[:dot1]
    return f"{dom1}\n{dom2}\n{dom3}"


web = input()
print(domen(web))