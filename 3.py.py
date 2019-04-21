import math
y=input("enter a number")
while (y !="x"):
    z=int(y)
    r=math.sqrt(z)
    j=int(r)
    k=j*j
    if(k==z):
        print("perfect square:")
    else:
        print("not perfect square")
    y=input("enter a number")
print("The End") 
