add=0
for i in range(100):
    a=int(input("Amount Is :"))
    c=input("do u want to continue? ")
    add += a
    if(c == "no" or c == "No"):
        break

print(add)
if(add<1000):
    print("Ther are no Discount ")
if(add>1000 and add<1500):
    print("3% Discount ")
    dis=add*0.03
    Total=add-dis
    print("Total Bill Is : ",Total)
elif(add>1500 and add<2000):
    print("5% Discount ")
    dis=add*0.05
    Total=add-dis
    print("Total Bill Is : ",Total)
elif(add>2000 and add<2500):
    print("7% Discount ")
    dis=add*0.07
    Total=add-dis
    print("Total Bill Is : ",Total)
elif(add>2500):
    print("10% Discount ")
    dis=add*0.10
    Total=add-dis
    print("Total Bill Is : ",Total)

