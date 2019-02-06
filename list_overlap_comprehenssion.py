import random
a= []
b= []
for i in range(random.randint(1,20)):
    a.append(random.randint(1,50))

for i in range(random.randint(1,20)):
    b.append(random.randint(1,50))

c=[]
print(a)
print(b)

c.append([x for x in b if x in a])

print(c)
