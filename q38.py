# Q38.. Write a Python program to drop empty Items from a given Dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

t={'c1': 'Red', 'c2': 'Green', 'c3': None}
d=t["c3"]
s={}
print(d)
for i in t:
    if d!=t[i]:
        s.update({i:t[i]})
print(s)
        

