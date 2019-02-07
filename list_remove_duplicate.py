import random

def func(a):
    c=[]
    [c.append(x) for x in a if x not in c]
    #c.append([x for x in a if x not in c]) #List comprehension here, does not work!
    #coz, the list 'c' is a temp list and is allways empty when compared.
    '''for i in range(len(a)):
        if a[i] not in c:
            c.append(a[i]);
            '''
    return c

a=[random.randint(1,5) for x in range(random.randint(6,10))]
print(a)

c = func(a)
print(c)
