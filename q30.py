# Q30.Write a Python program to remove spaces from dictionary keys.
# Original dictionary: {'S 001': ['Math', 'Science'], 'S 002': ['Math',
# 'English']}
# New dictionary: 
u={'S 001': ['Matinth', 'Science'], 'S  002': ['Math',
 'English']}
t={}
for i in u:
    sum=""
    for j in i:
        if j!=" ":
            sum=sum+j
    t.update({sum:u[i]})
print(t)
            


