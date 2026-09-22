import math
for x in range(10, 90, 5):
    a = 2*(x/100)**2 + 2
    b = (math.e**(-2*(x/100))) - (math.cos(1 - 2**(x/100)))
    c = math.log(2 * (x/100), 2)
    y = (a/b) + c
    print(y)


