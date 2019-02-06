import random
a = []
for i in range(random.randint(5,20)):
    a.append(random.randint(1,30))

c=[]

#c.append(x for x in a if x%2==0)
'''for x in a:
    if x%2==0:
        c.append(x)
'''
c.append([x for x in a if x%2== 0])
print(a)
#print(x for x in a if x%2==0)
print(c)
print(len(c))
