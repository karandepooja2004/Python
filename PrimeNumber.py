no=int(input("Enter Any Number : "))
i=2
flag=0
while(i<no):
    if(no%i==0):
        flag=1
        break
    i+=1
if(flag==0):
    print("Number Is Prime !!")
else:
    print("Number Is Not Prime !!")
