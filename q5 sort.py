# dic={"1":2,"3":4,"4":3,"2":1,0:0}
# li=[]
# g=[]
# for i in dic:
#     li.append(dic[i])
#     for j in range(len(li)):
#         for k in range(len(li)):
#             if li[j]<li[k]:
#                 li[j],li[k]=li[k],li[j]
# for l in li:
#     for h in dic:
#         if l==dic[h]:
#             a=h,l
#             g.append(a)
# print(g)

            

dic={"1":2,"3":4,"4":3,"2":1,0:0}
li=[]
g=[]
for i in dic:
    li.append(dic[i])
    for j in range(len(li)):
        for k in range(len(li)):
            if li[j]>li[k]:
                li[j],li[k]=li[k],li[j]
for l in li:
    for h in dic:
        if l==dic[h]:
            a=h,l
            g.append(a)
print(g)



# dic={"t":2,"3":4,"4":3,"2":1,0:0,"r":345,"67":789,"23":784,"23":2345}
# li=[]
# g=[]
# e={}
# for i in dic:
#     li.append(dic[i])
#     for j in range(len(li)):
#         for k in range(len(li)):
#             if li[j]>li[k]:
#                 li[j],li[k]=li[k],li[j]
# for l in range(len(li)):
#     if l==5:
#         break
#     t=li[l]
#     g.append(t)
# for i in g:
#     for k in dic:
#         if i==dic[k]:
#             e.update({k:i})
# print(e)        



            


            

