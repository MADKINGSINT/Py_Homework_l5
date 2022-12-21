n=3
sp=[]
for i in range(1,4):
    sp.append(input())
print(sp)
sp=list(filter(lambda x: "абв" not in x, sp))
print(sp)