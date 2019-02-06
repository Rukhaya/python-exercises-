import random
num= random.randint(1,100)

print("The devisors for ",num," are :");
for i in range(2,int(num/2)+1):
    if(num%i == 0):
        print(i)

