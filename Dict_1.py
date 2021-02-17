d = {}
d = dict

d = {"alex": 25, "Petr": 37}
print (d)

len(d)

d["KAte"] = 18
print(d)
print(d['Petr'])
d['KAte'] = 244
print(d['KAte'])
print(d)
d[10] = 20
print(d)

for key, value in d.items():
    print(key)
    print(value)

for key, value in d.items():
    print("ключ:" + str(key) + ",значення: " + str(value))
