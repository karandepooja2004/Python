Pass="@Pooja@123"
c=0
s=0
sy=0
n=0
w=0
x=len(Pass)
for i in range(len(Pass)):
    if(ord(Pass[i])>=65 and ord(Pass[i])<=90):
        c=1
    elif(ord(Pass[i])>=97 and ord(Pass[i])<=122):
        s=1
    elif((ord(Pass[i])>=58 and ord(Pass[i])<=64)):#or(ord(Pass[i])>=32 and ord(Pass[i])<=47)):
        sy=1
    elif(ord(Pass[i])>=48 and ord(Pass[i])<=57):
        n=1
if(x>8):
    w=1
if(c==1 and s==1 and sy==1 and n==1 and w==1):
    print("Your Entered Passward Is Valid !!")
else:
    print("Your Entered Passward Is Not Valid !!")
