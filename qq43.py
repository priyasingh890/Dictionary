# Q43.Write a Python program to create a dictionary grouping a sequence of key-value pairs
# into a dictionary of lists.
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
t=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
i=0
while i<len(t):
    j=0
    r=[]
    while j<len(t[i]):
            r.append(t[i][1])
            print(r)
            j=j+1
    print()
    i=i+1












    
        
       

