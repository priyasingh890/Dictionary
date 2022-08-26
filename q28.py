# Write a Python program to convert a list into a nested dictionary of keys.
# num_list = [1, 2, 3, 4]
# Sample output:
# {1: {2: {3: {4: {}}}}}
f={}
h={}
# t=[1, 2, 3, 4]
# i=1
# while i<=len(t):
#     f=({t[-i]:h})
#     i=i+1
#     print(f)


list = [1, 2, 3, 4]
dict = {}
i=1
while i<=len(list):
    dict = {list[-i]: dict}
    i=i+1
print(dict)


