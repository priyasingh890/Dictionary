#Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1',
#'amount': 750}]
#Expected Outp
data= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1',
'amount': 750}]
# g={}
# for i in data:
#     d=i["item"]
#     f=i["amount"]
# if f not in  g:
#         h={d:f} 
# else:
#         g[d]+=f
# print(g)

result = {}
for i in data:
    key = i['item']
    value = i['amount']
    if key not in result:
        temp = {key:value}
        result.update(temp)
    else:
        result[key] += value
print(result)


