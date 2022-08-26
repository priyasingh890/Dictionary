l={"5":2,"6":5,"8":6}
a=(input("enter no."))
if a in l.keys():
    del l[a]
    print(l)
else:
    l.update({a:a*2})
print(l)


# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# n = int(input('enter key'))
# if n in d.keys():
#     print('key already present')
# else:
#     d.update({n:n*2})
# print(d)