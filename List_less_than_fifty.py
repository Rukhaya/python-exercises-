import random
a = []

for i in range(10):
    a.append(random.randint(1,100));

for i in range(10):
    if a[i] < 50:
        print("a[",i,"]=",a[i])

