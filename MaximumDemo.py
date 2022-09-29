a=[63, 57, 83, 59, 78]
temp=a[0]
for i in range(1, len(a)):
    if(a[i]>temp):
        temp=a[i]
print("The maximum value is : ",temp)
