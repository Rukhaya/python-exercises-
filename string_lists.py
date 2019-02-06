buff = input("Enter string")
a = len(buff) // 2;
flag =1

for i in range(a):
    if(buff[i] != buff[(i*(-1))-1]):
            flag =0
            break;

if(flag == 1):
    print("palindrome");
else:
    print("Not palindrome");


'''def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
buff = input('Enter a continuous string-To check if it is Palindrome or not')
a= int(len(buff)/2)
print(a)

print(buff[0:a] )
print(reverse(buff[((a*(-1))) :]) )
print(buff[0:a] is reverse(buff[((a*(-1))-1) : ]) )
if (buff[0:a] is reverse(buff[((a*(-1))-1) : ]) ):
        print("PAlindrome:" +buff)
else:
        print("Not a PAlindrome:" +buff)
        '''

