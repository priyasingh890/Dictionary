# Q51.Write a Python program to filter even numbers from a given dictionary values.
# Original Dictionary:
# {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}
# Q52. Write a Python program to find the specified number of maximum values in a given
# t={'V': [, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}1, 4
t={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
w={}
for i in t:
    d=[]
    for j in range(len(t[i])):
        if t[i][j]%2==0:
            d.append(t[i][j])
        w.update({i:d})
print(w)

