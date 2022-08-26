# Q40. Write a Python program to convert more than one list to nested dictionary.
# Original strings:
# ['S001', 'S002', 'S003', 'S004']
# ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# [85, 98, 89, 92]
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}},
# {'S004': {'Saim Richards': 92}}

x=['S001', 'S002', 'S003', 'S004']
y=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
z=[85, 98, 89, 92]
g={}
for i in range(len(x)):
    g.update({x[i]:{y[i]:z[i]}})
print(g)
    


