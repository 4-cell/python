a = [1,2,3,4,5,6,7,8]
b = [1,2,3]

for outindex in range(len(a)-len(b)+ 1):
    total = 0
    for inIndex in range(len(b)):
        total += a[inIndex + outindex] * b[inIndex]

    print(total)