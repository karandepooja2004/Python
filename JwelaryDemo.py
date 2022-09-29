add=0
print("**********WELCOME IN MY JWELARY SHOP***********\n")
for i in range(100):
    a=int(input("Weight In Gram Is :"))
    x=52000
    #print("Price Of 10 Gram Gold Is : ",x)
    p=x/10
    #print("Price Of Per Gram Gold Is : ",p)
    price=a*p
    #print("Price Of Entered Gold Is : ",price)
    GST=price+(price*0.03)
    WorkAmount=GST+400
    add=add+WorkAmount
    c=input("do u want to continue? ")
    if(c == "no" or c == "No"):
        break
print("\n---------------------------\n")
print("Total Amount Is : ",add,"\n")
if(add<50000):
    print("Ther are no Discount ")
if(add>50000 and add<75000):
    print("3% Discount ")
    dis=add*0.03
    Total=add-dis
    print("Total Bill Is : ",Total)
elif(add>75000 and add<90000):
    print("5% Discount ")
    dis=add*0.05
    Total=add-dis
    print("Total Bill Is : ",Total)
elif(add>90000 and add<100000):
    print("7% Discount ")
    dis=add*0.07
    Total=add-dis
    print("Total Bill Is : ",Total)
elif(add>100000):
    print("10% Discount ")
    dis=add*0.10
    Total=add-dis
    print("Total Bill Is : ",Total)
    

