
aarray = [
    [1, 2],
    [3, 4],
    [5, 6]
] 

barray = [
    [5, 6],
    [7, 8]
]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(aarray)): 
    for j in range(len(barray[0])): 
        for k in range(len(barray)):
          result[i][j] +=aarray[i][k] * barray[k][j]

for row in result:
    print(row)