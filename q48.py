# Q48.Write a Python program to find the length of a given dictionary values.
# Original Dictionary:
# {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}
# t={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# d={}
# for i in t:
#     s=len(t[i])
#     d.update({t[i]:s})
#     print(d)
s={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
w={}
for i in s:
    sum=""
    for j in range(len(s[i])):
        if s[i][j]!=" ":
            sum=sum+s[i][j]
            d=len(sum)
        w.update({s[i]:d})
print(w)
        
