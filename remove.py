s={"key":100,"rule":100,"rr":300}
u={}
for i in s:
    if s[i]not in u.values():
        u.update({i:s[i]})
        print(u)