count = int(input())
dx = 0
dy = 0
xFlag = True
yFlag = False
xC = -1
yC = -1
xm = 1
ym = 1
x = 0
y = 0
for i in range(count):
    if xC:
        dx += 1 * xC
        x += 1
        if x == xm:
            xC = False
            yFlag = True
            xC *= -1
            xm += 1
            a = 0
    else:
        dy += 1 * yC
        y += 1
        if y == ym:
            yFlag = False
            xC = True
            yC *= -1
            ym += 1
            y = 0
print(dx, dy)
