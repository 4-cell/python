a = [-4, 8, -6, 11, -9]

for I in range(len(a)):
    for J in range(I+1,len(a)):
        if a[I] + a[J] == 4:
            print ("I =", a[I])
            print ("J =", a[J])