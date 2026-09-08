a = [9, 9, 5] 
b = [9, 9, 2]

c = [0, 0, 0]
carry = 0

for i in range(len(a)):
    c[i] = a[i] + b[i] + carry
    if c[i] >= 10:
        c[i] -= 10
        carry = 1
    else:
        carry = 0
    
if carry == 1:
    c.append(1)    
print(c)