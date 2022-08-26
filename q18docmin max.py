dic={34:45,56:23,67:24,78:99,4:89}
lis=[]
for i in dic :
    lis.append(dic[i])
i=0
max=lis[i]
max2=lis[i]
while i<len(lis):
    if max<lis[i]:
        max=lis[i]
    elif max2>lis[i]:
        max2=lis[i]
    i=i+1
print(max)
print(max2)


