
cars = ["Ford", "Volvo", "BMW","Ferrari","Lambroghini","Honda"]

maxlen = 0
longest = ""

for comp in cars:

    if maxlen < len(comp):
       maxlen = len(comp)
       longest = comp

print(maxlen)
print(longest)