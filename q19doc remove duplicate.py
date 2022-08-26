# dic={"23":100,"34":100,"20":27,"3":100,"45":400}
# d={}
# for i in dic:
#     if dic[i] not in d.values():
#         d[i]=dic[i]
# print(d)


data={"id1":
{"name":["sara"],
"class":["v"],
"subject_integration":["english","math","science"]
},
"id2":
{"name":["david"],
"class":["v"],
"subject_integration":["english","math","science"]
},
"id3":
{"name":["sara"],
"class":["v"],
"subject_integration":["english","math","science"]},
"id4":
{"name":["suraya"],                                                                                                   
"class":["v"],
"subject_integration":["english","math","science"]
},
}
g={}
for i in data:
    if data[i] not in g.values():
        g[i]=data[i]
print(g)