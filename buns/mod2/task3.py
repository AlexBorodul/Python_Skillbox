def middle(num):
    a = int(num[0:num.find(' ')])
    b = int(num[num.find(' ')+1:num.rfind(' ')])
    c = int(num[num.rfind(' ')+1::])
    if (b <= a <= c) or (c <= a <= b):
        print(a)
    elif (a <= b <= c) or (c <= b <= a):
        print(b)
    else:
        print(c)

num = input()
middle(num)
input()