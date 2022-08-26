d1={"a":100,"b":200,"c":300}
d2={"a":300,"b":200,"d":400}
g={}
for i in d1:
    for j in d2:
        if i==j:
            d1[i]=d1[i]+d2[j]
        else:
            d1[i]=d1[i]
            d1[i]=d2[j]
print(d1)

#     if  i in d2:
#         d1[i]=d1[i]+d2[i]
#     else:
#         d1[i]=d1[i]
#         d1[i]=d2[i]
# print(d1)
# # a="gfjf"*-1
# print(a)


            




    

