
# A Python Dictionary contains List as value. Write a Python program to clear the list values in
# the said dictionary.
# Original Dictionary:
# {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# Clear the list values in the said dictionary:
# {'C1': [], 'C2': [], 'C3': []}
r={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
d={}
for i in range(0,3):
    for j in r:
        d.update({j:[]})
if i==2:
        d.update({j:r[j]})
print(d)
