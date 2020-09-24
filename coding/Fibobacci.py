a, b = 0, 1
while b <= 10000:
    print(b, end=",")
    m = b
    b = a+b
    a = m

