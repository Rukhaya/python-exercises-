import random
a= []
b= []
for i in range(random.randint(1,20)):
    a.append(random.randint(1,50))

for i in range(random.randint(1,20)):
    b.append(random.randint(1,50))

c=[]
for i in range(len(b)):
    if(  b[i] in a ):
        c.append(b[i])

print(a)
print(b)
print(c)
