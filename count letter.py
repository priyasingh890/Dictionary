# output{"w":1,"3":1,"r":2,"s":1,"o":1,"u":1,"c":1}
string="w3resourcee"
k={}
for i in string:
    if i not in k:
        k[i]=1
    else:
        k[i]+=1
print(k)

