s={"riya":34,"siya":56,"diya":23,"mahima":67}
w={}
for i in s:
    f={}
    for j in s:
        f={i:s[i]}
        w.update({i:f})
print(w)