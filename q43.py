
# Write a Python program to check all values are same in a dictionary. Go to the editor
# Original Dictionary:
# {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# Check all are 12 in the dictionary.
# True
# Check all are 10 in the dictionary.
# False

g={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
h=[]
c=0
d=g["Cierra Vega"]
for i in g:
    if d==g[i]:
        c=c+1
if c==len(g):
    print("true")
else:
    print('false')



