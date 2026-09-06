a = [1, 2, -1, 3, -5, 7, -2, 4, 6, -8, 9, -3, 5, -7, 10, -4, 8, -6, 11, -9]

for I in range(len(a)):
    for J in range(I+1,len(a)):
        if a[I]+a[J] == 4:
            print ("I =", a[I])
            print ("J =", a[J])
