result = { ('r','p'):0 , ('p','r'):1 , ('r','s'):1 , ('s','r'):0 , ('s','p'):1 , ('p','s'):0 }

def call_result(a,b):
    print( (a,b) in result )
    print( (a,b) not in result )
    if( (a,b) in result ):
        return result[(a,b)]
    else:
        flag=0
        return 1


while(1):
    flag= 1
    print("Welcome to rock paper sissor")
    str1=input("Playe 1  name: \n")
    str2=input("Playe 2  name: \n")
    print('r-rock p-paper s-sissor')
    p1=input("1 : \n")
    p2=input("2 : \n")
    if(call_result(p1,p2)):
        if(flag):
            print(str1,' beats ',str2)
        else:
            print(str1,' and ',str2, 'TIED!')
    else:
        print(str2,' beats ',str1)

    if(input('Do you want to play again?(y/any key)') !='y'):
        break

print('Thank you ! END')


