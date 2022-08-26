# 44.Write a Python program to split a given dictionary of lists into list of dictionaries.
# Original dictionary of lists:
# ce': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}{'Scien
# Split said dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language':
# 84}, {'Science': 95, 'Language': 80}]



# t={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# for i in t:
#     for j in range(len(t[i])):
#         for k in range(len(t[i])):


d= {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
f=[]
for i in range(0,4):
    e={}
    for r in d:
        for j in d:
            print(d[j])
            if r==j:
                e.update({j:d[j][i]})
    f.append(e)
print(f)



        












