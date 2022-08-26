# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
z=[]
for i in d:
    s=[]
    s.append(i)
    s.append(d[i])
    z.append(s)
print(z)




