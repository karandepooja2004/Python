a=[33, 89, 90, 28, 85, 88]
i=0
Sum=0
flag=0
while(i<len(a)):
    if(a[i]<35):
        flag+=1
    Sum+=a[i]
    i+=1
print("Total Of All Subjects : ", Sum)
per=Sum/5
print("Percentage Is : ", per)
elif(flag>0 and flag<3):
    print("AT KT")
    print("You Are fail In ",flag,"Subjects")
elif(flag>2):
    print("Fail!!")
elif(per>=35 and per<50):
    print("Pass!!")
elif(per>=50 and per<60):
    print("Second Class!!")
elif(per>=60 and per<75):
    print("Frist Class!!")
elif(per>=75 and per<=100):
    print("First Class With Distinction!!")

    
