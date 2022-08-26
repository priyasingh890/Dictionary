# Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:20}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 40, 3: 30, 5: 50, 6: 60}



dic1={1:10, 2:20}
dic2={3:30, 2:40}
dic3={5:50,6:60}
for i in dic2:
    if i in dic1:
        dic1[i]=dic1[i]+dic2[i]
    else:
        dic1[i]=dic2[i]
        dic1.update(dic3)
print(dic1)
