# .Write a Python program to match 
# Expected output: key1: 1 is present in both x and ykey values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
t={'key1': 1, 'key2': 3, 'key3': 2}
y={'key1': 1, 'key2': 2}
b={}
for i in t:
    for j in y:
        if t[i]==y[j] and i==j:
            b.update({j:y[j]})
print(b)
    






